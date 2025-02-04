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

#  [AudioSource](AudioSource.html).loop

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

public bool loop;

### Description

Checks if the audio clip is looping

Return or set whether the audio clip replays after it finishes playing.
Disable looping on a playing AudioSource to stop the sound after the end of
the current loop. Use the checkbox in the AudioSource component to enable or
disable looping without code.

    
    
    //Create an empty [GameObject](GameObject.html) and attach this script
    //Attach an [AudioSource](AudioSource.html) component. (Click on the [GameObject](GameObject.html), go to its Inspector and click **Add Component** [Button](UIElements.Button.html). Go to **Audio** >**Audio Source**)
    //Attach an Audio clip in the [AudioClip](AudioClip.html) field of the [AudioSource](AudioSource.html)
    //Create a [Button](UIElements.Button.html) (**Create** >**UI** >**Button**) and a [Toggle](UIElements.Toggle.html) (**Create** >**UI** >**Toggle**). Attach these in the Inspector of your [GameObject](GameObject.html).  
      
    //This script allows you to toggle the loop of a sound on or off
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class AudioSourceLoop : [MonoBehaviour](MonoBehaviour.html)
    {
        [AudioSource](AudioSource.html) m_AudioSource;  
      
        public [Toggle](UIElements.Toggle.html) m_Toggle;
        public [Button](UIElements.Button.html) m_Button;  
      
        void Start()
        {
            //Fetch the [AudioSource](AudioSource.html) component of the [GameObject](GameObject.html) (make sure there is one in the Inspector)
            m_AudioSource = GetComponent<[AudioSource](AudioSource.html)>();
            //Stop the Audio playing
            m_AudioSource.Stop();
            //Call the PlayButton function when you click this [Button](UIElements.Button.html)
            m_Button.onClick.AddListener(PlayButton);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Turn the loop on and off depending on the [Toggle](UIElements.Toggle.html) status
            m_AudioSource.loop = m_Toggle.isOn;
        }  
      
        //This plays the Audio clip when you press the [Button](UIElements.Button.html)
        void PlayButton()
        {
            m_AudioSource.Play();
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

