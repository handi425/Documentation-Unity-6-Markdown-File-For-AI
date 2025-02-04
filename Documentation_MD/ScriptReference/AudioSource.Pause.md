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

#  [AudioSource](AudioSource.html).Pause

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

public void Pause();

### Description

Pauses playing the [clip](AudioSource-clip.html).

Additional resources: [Play](AudioSource.Play.html),
[Stop](AudioSource.Stop.html) functions.

    
    
    // Allow a song to be chosen and played.  If can be paused, and the song played further.
    // Two songs are supported.  
      
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // two clips, perhaps songs for the game
        public [AudioClip](AudioClip.html) song1;
        public [AudioClip](AudioClip.html) song2;  
      
        private [AudioSource](AudioSource.html) audioSource;
        private bool paused1;
        private bool paused2;  
      
        // both songs are in paused state
        void Start()
        {
            audioSource = GetComponent<[AudioSource](AudioSource.html)>();
            paused1 = true;
            paused2 = true;
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 200, 100), "Play song1"))
            {
                if (paused1 && paused2)
                {
                    audioSource.clip = song1;
                    audioSource.Play(0);
                    paused1 = false;
                }
            }  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(250, 10, 200, 100), "Pause song1"))
            {
                if (paused1 == false)
                {
                    audioSource.Pause();
                    paused1 = true;
                }
            }  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 180, 200, 100), "Play song2"))
            {
                if (paused2 && paused1)
                {
                    audioSource.clip = song2;
                    audioSource.Play(0);
                    paused2 = false;
                }
            }  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(250, 180, 200, 100), "Pause song2"))
            {
                if (paused2 == false)
                {
                    audioSource.Pause();
                    paused2 = true;
                }
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

