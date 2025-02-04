[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [AudioSource](AudioSource.html).pitch

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-AudioSource.html "Go to AudioSource
Component in the Manual")

public float pitch;

### Description

The pitch of the audio source.

Pitch makes a melody go higher or lower. For example, if you play an audio
clip with pitch set to one, increasing the pitch as the clip plays will make
the clip sound higher. Similarly, decreasing the pitch to less than one makes
the clip sound lower. When [resource](AudioSource-resource.html) is an
[AudioClip](AudioClip.html), the pitch property is clamped to the range
[-3..3]. When [resource](AudioSource-resource.html) is an
AudioRandomContainer, the pitch property is ignored, and if it is not in the
range [0.0001..3.0], a warning appears in the console. This is due to
AudioRandomContainer not supporting reverse/pause playback from the pitch. Any
values outside this range are clamped when changing from an
[AudioClip](AudioClip.html) to an AudioRandomContainer.

    
    
    //Attach this script to a [GameObject](GameObject.html).
    //Attach an [AudioSource](AudioSource.html) to your [GameObject](GameObject.html) (Click **Add Component** and go to **Audio** >**Audio Source**). Choose an audio clip in the **AudioClip** field.
    //This script sets the pitch of the audio at the start, and then gradually turns it down to 0 as time passes.  
      
    using UnityEngine;  
      
    //Make sure there is an Audio Source component on the [GameObject](GameObject.html)
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public int startingPitch = 4;
        public int timeToDecrease = 5;
        [AudioSource](AudioSource.html) audioSource;  
      
        void Start()
        {
            //Fetch the [AudioSource](AudioSource.html) from the [GameObject](GameObject.html)
            audioSource = GetComponent<[AudioSource](AudioSource.html)>();  
      
            //Initialize the pitch
            audioSource.pitch = startingPitch;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //While the pitch is over 0, decrease it as time passes.
            if (audioSource.pitch > 0)
            {
                audioSource.pitch -= [Time.deltaTime](Time-deltaTime.html) * startingPitch / timeToDecrease;
            }
        }
    }
    

Another example:

    
    
    using UnityEngine;  
      
    // A script that plays your chosen song.  The pitch starts at 1.0.
    // You can increase and decrease the pitch and hear the change
    // that is made.  
      
    public class AudioExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float pitchValue = 1.0f;
        public [AudioClip](AudioClip.html) mySong;  
      
        private [AudioSource](AudioSource.html) audioSource;
        private float low = 0.75f;
        private float high = 1.25f;  
      
        void Awake()
        {
            audioSource = GetComponent<[AudioSource](AudioSource.html)>();
            audioSource.clip = mySong;
            audioSource.loop = true;
        }  
      
        void OnGUI()
        {
            pitchValue = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 75, 100, 30), pitchValue, low, high);
            audioSource.pitch = pitchValue;
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

