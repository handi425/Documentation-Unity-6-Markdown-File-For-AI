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

#  [AudioSource](AudioSource.html).Stop

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

## Declaration

public void Stop();

### Description

Stops playing the [clip](AudioSource-clip.html).

The AudioSource.stop function stops the currently set Audio clip from playing.
The Audio clip plays from the beginning the next time you play it.  
  
Additional resources: [Play](AudioSource.Play.html),
[Pause](AudioSource.Pause.html) functions.

    
    
    //This script allows you to toggle music to play and stop.
    //Assign an [AudioSource](AudioSource.html) to a [GameObject](GameObject.html) and attach an Audio Clip in the Audio Source. Attach this script to the [GameObject](GameObject.html).  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [AudioSource](AudioSource.html) m_MyAudioSource;  
      
        //Play the music
        bool m_Play;
        //Detect when you use the toggle, ensures music isn’t played multiple times
        bool m_ToggleChange;  
      
        void Start()
        {
            //Fetch the [AudioSource](AudioSource.html) from the [GameObject](GameObject.html)
            m_MyAudioSource = GetComponent<[AudioSource](AudioSource.html)>();
            //Ensure the toggle is set to true for the music to play at start-up
            m_Play = true;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Check to see if you just set the toggle to positive
            if (m_Play == true && m_ToggleChange == true)
            {
                //Play the audio you attach to the [AudioSource](AudioSource.html) component
                m_MyAudioSource.Play();
                //Ensure audio doesn’t play more than once
                m_ToggleChange = false;
            }
            //Check if you just set the toggle to false
            if (m_Play == false && m_ToggleChange == true)
            {
                //Stop the audio
                m_MyAudioSource.Stop();
                //Ensure audio doesn’t play more than once
                m_ToggleChange = false;
            }
        }  
      
        void OnGUI()
        {
            //[Switch](PlayerSettings.Switch.html) this toggle to activate and deactivate the parent [GameObject](GameObject.html)
            m_Play = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(10, 10, 100, 30), m_Play, "Play Music");  
      
            //Detect if there is a change with the toggle
            if ([GUI.changed](GUI-changed.html))
            {
                //Change to true to show that there was just a change in the toggle state
                m_ToggleChange = true;
            }
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

