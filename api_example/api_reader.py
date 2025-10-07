import requests
import pandas as pd

class RickAndMortyAPIReader:
    def __init__(self, base_url: str = "https://rickandmortyapi.com/api"):
        self.base_url = base_url
        self.characters_url = f"{base_url}/character"

    def get_all_characters(self) -> pd.DataFrame:
        """
        Получает всех персонажей из API и возвращает в виде DataFrame
        """
        all_characters = []
        next_page = self.characters_url

        while next_page:
            response = requests.get(next_page)

            if response.status_code != 200:
                raise Exception(f"Ошибка API: {response.status_code}")

            data = response.json()
            characters = data['results']
            all_characters.extend(characters)

            next_page = data['info']['next']

        df = pd.DataFrame(all_characters)

        # Обработка вложенных колонок (origin, location, episode)
        if 'origin' in df.columns:
            origin_df = pd.json_normalize(df['origin'])
            origin_df.columns = [f"origin_{col}" for col in origin_df.columns]
            df = pd.concat([df, origin_df], axis=1)

        if 'location' in df.columns:
            location_df = pd.json_normalize(df['location'])
            location_df.columns = [f"location_{col}" for col in location_df.columns]
            df = pd.concat([df, location_df], axis=1)

        if 'episode' in df.columns:
            df['episodes_count'] = df['episode'].apply(len)
            df['episodes'] = df['episode'].apply(lambda x: [ep.split('/')[-1] for ep in x])

        df = df.drop(columns=[col for col in ['origin', 'location', 'episode'] if col in df.columns])

        return df

if __name__ == "__main__":
    api_reader = RickAndMortyAPIReader()
    try:
        print("Загрузка всех персонажей...")
        all_characters_df = api_reader.get_all_characters()
        print(f"Загружено {len(all_characters_df)} персонажей\n")
        print("Первые 5 записей:")
        print(all_characters_df[['name', 'status', 'species', 'gender']].head())

        print("\nСтатистика по статусам:")
        print(all_characters_df['status'].value_counts())

        print("\nСтатистика по видам (species):")
        print(all_characters_df['species'].value_counts().head(10))

    except Exception as e:
        print(f"Произошла ошибка: {e}")
