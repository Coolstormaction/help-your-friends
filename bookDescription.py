import requests
class bookDescription:
    hp = "Harry Potter"
    ta = "The Alchemist"
    thotb = "The Hound of the Baskervilles"
    rdpd = "Rich Dad Poor Dad"
    h_isA = True
    a_isA = False
    s_isH = False
    r_isA = False
    
    def harry_potter():
        harry_potter_text = '''
            Mr. and Mrs. Dursley, of number four, Privet Drive, were
            proud to say that they were perfectly normal, thank
            you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t
            hold with such nonsense.
            Mr. Dursley was the director of a fi rm called Grunnings, which
            made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin
            and blonde and had nearly twice the usual amount of neck, which
            came in very useful as she spent so much of her time craning over
            garden fences, spying on the neighbors. The Dursleys had a small
            son called Dudley and in their opinion there was no fi ner boy
            anywhere.
            The Dursleys had everything they wanted, but they also had a
            secret, and their greatest fear was that somebody would discover it. 
        '''
        return harry_potter_text
    
    def the_alchemist():
        
        the_alchemist = '''
            THE BOY’S NAME WAS SANTIAGO. DUSK WAS FALLING AS the boy arrived
            with his herd at an abandoned church. The roof had fallen in long
            ago, and an enormous sycamore had grown on the spot where the
            sacristy had once stood.
            He decided to spend the night there. He saw to it that all the
            sheep entered through the ruined gate, and then laid some planks
            across it to prevent the flock from wandering away during the night.
            There were no wolves in the region, but once an animal had strayed
            during the night, and the boy had had to spend the entire next day
            searching for it.
            He swept the floor with his jacket and lay down, using the book
            he had just finished reading as a pillow. He told himself that he
            would have to start reading thicker books: they lasted longer, and
            made more comfortable pillows.
            It was still dark when he awoke, and, looking up, he could see
            the stars through the half-destroyed roof.
            I wanted to sleep a little longer, he thought. He had had the same
            dream that night as a week ago, and once again he had awakened
            before it ended.
            He arose and, taking up his crook, began to awaken the sheep
            that still slept. He had noticed that, as soon as he awoke, most of his
            animals also began to stir. It was as if some mysterious energy
            bound his life to that of the sheep, with whom he had spent the past
            two years, leading them through the countryside in search of food
            and water. “They are so used to me that they know my schedule,” he
            muttered. Thinking about that for a moment, he realized that it
            could be the other way around: that it was he who had become
            accustomed to their schedule.

        '''
        print(len(the_alchemist))

    def sh_holmes():
        
        the_hound_of_the_baskervilles = '''
            Mr. Sherlock Holmes, who was usually very late in the
            mornings, save upon those not infrequent occasions
            when he was up all night, was seated at the breakfast table.
            I stood upon the hearth-rug and picked up the stick which
            our visitor had left behind him the night before. It was a
            fine, thick piece of wood, bulbous-headed, of the sort which
            is known as a ‘Penang lawyer.’ Just under the head was a
            broad silver band nearly an inch across. ‘To James Mortimer, M.R.C.S., from his friends of the C.C.H.,’ was engraved
            upon it, with the date ‘1884.’ It was just such a stick as the
            old-fashioned family practitioner used to carry—dignified,
            solid, and reassuring.
            ‘Well, Watson, what do you make of it?’
            Holmes was sitting with his back to me, and I had given
            him no sign of my occupation.
            ‘How did you know what I was doing? I believe you have
            eyes in the back of your head.’
            ‘I have, at least, a well-polished, silver-plated coffee-pot
            in front of me,’ said he. ‘But, tell me, Watson, what do you
            make of our visitor’s stick? Since we have been so unfortu-
        '''
        return the_hound_of_the_baskervilles

    def rich_dad_poor_dad():
        
        rich_dad_and_poor_dad = '''
            There is a Need
            Does school prepare children for the real world? “Study hard and get good grades and you will
            find a high-paying job with great benefits,” my parents used to say. Their goal in life was to
            provide a college education for my older sister and me, so that we would have the greatest
            chance for success in life. When I finally earned my diploma in 1976-graduating with honors,
            and near the top of my class, in accounting from Florida State University-my parents had
            realized their goal. It was the crowning achievement of their lives. In accordance with the
            “Master Plan,” I was hired by a “Big 8” accounting firm, and I looked forward to a long career
            and retirement at an early age.
            My husband, Michael, followed a similar path. We both came from hardworking families, of
            modest means but with strong work ethics. Michael also graduated with honors, but he did it
            twice: first as an engineer and then from law school. He was quickly recruited by a prestigious
            Washington, D.C., law firm that specialized in patent law, and his future seemed bright, career
            path well-defined and early retirement guaranteed.
            Although we have been successful in our careers, they have not turned out quite as we
            expected. We both have changed positions several times-for all the right reasons-but there are
            no pension plans vesting on our behalf. Our retirement funds are growing only through our
            individual contributions.
            Michael and I have a wonderful marriage with three great children. As I write this, two are in
            college and one is just beginning high school. We have spent a fortune making sure our children
            have received the best education available.
            One day in 1996, one of my children came home disillusioned with school. He was bored and
            tired of studying. “Why should I put time into studying subjects I will never use in real life?” he
            protested.
            Without thinking, I responded, “Because if you don't get good grades, you won't get into
            college.” “Regardless of whether I go to college,” he replied, “I'm going to be rich.”
            “If you don't graduate from college, you won't get a good job,” I responded with a tinge of panic
            and motherly concern. “And if you don't have a good job, how do you plan to get rich?”
            My son smirked and slowly shook his head with mild boredom. We have had this talk many
            times before. He lowered his head and rolled his eyes. My words of motherly wisdom were
            falling on deaf ears once again.
            Though smart and strong-willed, he has always been a polite and respectful young man.
            “Mom,” he began. It was my turn to be lectured. “Get with the times! Look around; the richest
            people didn't get rich because of their educations. Look at Michael Jordan and Madonna. Even
            Bill Gates, who dropped out of Harvard, founded Microsoft; he is now the richest man in
        '''
        return rich_dad_and_poor_dad

# print(bookDescription.the_alchemist())