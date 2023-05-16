## Hößl & Müller (19.5/20P)

### 1 Reading (5/5P)

 * common use cases for machine learning (2P)
   * a bit sparse for Scully, but ok
 * problems of machine learning (2P)
   * well done
 * authors' credentials (1P)
   * well done

### 2 Gathering Training Data (6/6P)

 * data logged correctly
   * looks good (+2)
 * proper name and structure
   * whitespace-separated CSVs are strange, but as long as it works *shrug* (+2)
 * logging started with DIPPID
   * yes (+1)
 * enough log data
   * yes (+1)

### 3 Activity Recognition (8.5/9P)

 * load training data
   * yes (+1)
 * pre-process training data
   * fft seems appropriate (+2)
 * train classifier
   * yes (+1)
 * correct predictions
   * why did you use a linear kernel?
   * works in most cases and independet of phone's orientation (+2.5)
   * there are short periods of misclassifications in between (-0.5)
 * continuous prediction
   * works (+1)
 * nice visualization
   * yes (+1)

*Warning:* Your repo is quite messy and your README is misleading.
Thought I could start activity-recognizer.py - but it doesn't even have an `if __name__ == '__main__'` block.
You get a pass this time, but you will lose points next time.
