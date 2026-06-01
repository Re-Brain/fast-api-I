from database import SessionLocal, engine
from models import Horse, Base

# Drop old table and recreate with new schema
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

db = SessionLocal()

horses = [
    Horse(name="Deep Impact", title="Sunday Silence's Best Prodigy", img="/horses/001.jpg", age=6, record="14-3-2", trainer="Yasuo Ikee"),
    Horse(name="Orfevre", title="The Golden Tyrant", img="/horses/002.jpg", age=5, record="12-2-1", trainer="Makoto Sakaguchi"),
    Horse(name="Kitasan Black", title="The Festival Horse", img="/horses/003.jpg", age=7, record="16-4-2", trainer="Yukio Hagiwara"),
    Horse(name="Symboli Rudolf", title="The Emperor", img="/horses/004.jpg", age=5, record="13-2-0", trainer="Makoto Kaneko"),
    Horse(name="T.M. Opera O", title="Centurial Overlord", img="/horses/005.jpg", age=5, record="14-4-2", trainer="Iwao Okamoto"),
    Horse(name="Special Week", title="Supreme Commander of Japan", img="/horses/006.jpg", age=5, record="10-3-2", trainer="Shigetaka Sakamoto"),
    Horse(name="Equinox", title="The World Class", img="/horses/007.jpg", age=4, record="10-1-1", trainer="Tetsuya Kimura"),
    Horse(name="Forever Young", title="The Most Dominated Dirt Horse of Japan", img="/horses/008.jpg", age=3, record="7-1-0", trainer="Hideyuki Mori"),
    Horse(name="Almond Eye", title="Fastest Mare in Japan History", img="/horses/009.jpg", age=6, record="15-3-1", trainer="Sakae Kunieda"),
]

db.add_all(horses)
db.commit()
db.close()

print("Done!")
