import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
			   "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
			   "avatar_poster.jpg",
			   "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
			   )

titanic = media.Movie("Titanic",
				"A seventeen-year-old aristocrat falls in love with a kind, but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
				"titanic_poster.jpg",
				"https://www.youtube.com/watch?v=2e-eXJ6HgkQ"
				)

star_wars = media.Movie("Star Wars Ep. VII: The Force Awakens",
				"Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along with the help of the Resistance.",
				"star_wars_poster.jpg",
				"https://www.youtube.com/watch?v=sGbxmsDFVnE"
				)

jurassic_world = media.Movie("Jurassic World",
				"A new theme park is built on the original site of Jurassic Park. Everything is going well until the park's newest attraction--a genetically modified giant stealth killing machine--escapes containment and goes on a killing spree.",
				"jurassic_world_poster.jpg",
				"https://www.youtube.com/watch?v=RFinNxS5KN4"
				)

the_avengers = media.Movie("The Avengers",
				"Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
				"the_avengers_poster.jpg",
				"https://www.youtube.com/watch?v=eOrNdBpGMv8"
				)

furious_7 = media.Movie("Furious 7",
				"Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.",
				"furious_7_poster.jpg",
				"https://www.youtube.com/watch?v=Skpu5HaVkOc"
				)

the_avengers_ultron = media.Movie("The Avengers: Age of Ultron",
				"When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping program called Ultron, things go horribly wrong and it's up to Earth's Mightiest Heroes to stop the villainous Ultron from enacting his terrible plans.",
				"the_avengers_poster.jpg",
				"https://www.youtube.com/watch?v=tmeOjFno6Do"
				)

harry_potter_hallows = media.Movie("Harry Potter and the Deathly Hallows: Part II",
				"Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.",
				"harry_potter_hallows_poster.jpg",
				"https://www.youtube.com/watch?v=I_kDb-pRCds"
				)
frozen = media.Movie("Frozen",
				"When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.",
				"frozen_poster.jpg",
				"https://www.youtube.com/watch?v=TbQm5doF_Uc"
				)

movies = [avatar, titanic, star_wars, jurassic_world, the_avengers, furious_7, the_avengers_ultron, harry_potter_hallows, frozen]

fresh_tomatoes.open_movies_page(movies)



