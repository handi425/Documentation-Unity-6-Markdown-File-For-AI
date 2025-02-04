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

#  [AudioSource](AudioSource.html).Play

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

public void Play(ulong delay = 0);

### Parameters

delay | Deprecated. Delay in number of samples, assuming a 44100Hz sample rate (meaning that Play(44100) will delay the playing by exactly 1 sec).  
---|---  
  
### Description

Plays the [clip](AudioSource-clip.html).

The delay parameter is deprecated, please use the newer
[AudioSource.PlayDelayed](AudioSource.PlayDelayed.html) function instead which
specifies the delay in seconds.  
  
If [AudioSource.clip](AudioSource-clip.html) is set to the same clip that is
playing then the clip will sound like it is re-started.
[AudioSource](AudioSource.html) will assume any [Play](AudioSource.Play.html)
call will have a new audio clip to play.  
  
**Note:** The [AudioSource.PlayScheduled](AudioSource.PlayScheduled.html) API
will give you more accurate control over when the audio clip is played.

    
    
    using UnityEngine;  
      
    // The Audio Source component has an [AudioClip](AudioClip.html) option.  The audio
    // played in this example comes from [AudioClip](AudioClip.html) and is called audioData.  
      
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [AudioSource](AudioSource.html) audioData;  
      
        void Start()
        {
            audioData = GetComponent<[AudioSource](AudioSource.html)>();
            audioData.Play(0);
            [Debug.Log](Debug.Log.html)("started");
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 70, 150, 30), "Pause"))
            {
                audioData.Pause();
                [Debug.Log](Debug.Log.html)("Pause: " + audioData.time);
            }  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 170, 150, 30), "Continue"))
            {
                audioData.UnPause();
            }
        }
    }
    

Additional resources: [Stop](AudioSource.Stop.html),
[Pause](AudioSource.Pause.html), [clip](AudioSource-clip.html) and
[PlayScheduled](AudioSource.PlayScheduled.html) functions.

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

