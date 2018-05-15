# Patrick Emami
# 
# Generates the boiler-plate for a new paper summary
import datetime
import os

if __name__ == '__main__':
    # Find out the topic
    topic_code = input("What topic does this paper fall under?\n\t(1) AGI\n\t(2) computer vision\n\t(3) deep learning theory\n\t(4) deep RL\n\t(5) general ML\n\t(6) GANs\n\t(7) NLP\n\t(8) RL theory\n")
    topic_code = int(topic_code)
    if topic_code == 1:
        topic = "AGI"
    elif topic_code == 2:
        topic = "computer-vision"
    elif topic_code == 3:
        topic = "deep-learning-theory"
    elif topic_code == 4:
        topic = "deep-RL"
    elif topic_code == 5:
        topic = "general-ML"
    elif  topic_code == 6:
        topic = "generative-adversarial-networks"
    elif topic_code == 7:
        topic = "natural-language-processing"
    elif topic_code == 8:
        topic = "reinforcement-learning-theory"
    else:
        print("[!] Unknown topic")
        exit(1)
    
    fn = input("Provide a shortened title for the URL:\n")
    # Find out today's date in %YYYY-MM-DD format
    date = datetime.date.today().strftime("%Y-%m-%d")

    fn = os.path.join('paper-summaries', topic, '_posts', date + '-' + fn + '.markdown')

    with open(fn, 'w+') as new_paper_sum:
        with open(os.path.join('_drafts', 'paper-summaries-template.md'), 'r') as template:
            import pdb; pdb.set_trace()
            t = template.read()
            new_paper_sum.write(t)

      
