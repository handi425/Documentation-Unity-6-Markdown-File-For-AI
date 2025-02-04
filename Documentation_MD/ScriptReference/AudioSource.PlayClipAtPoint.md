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

#  [AudioSource](AudioSource.html).PlayClipAtPoint

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

public static void PlayClipAtPoint([AudioClip](AudioClip.html) clip,
[Vector3](Vector3.html) position, float volume = 1.0F);

### Parameters

clip | Audio data to play.  
---|---  
position | Position in world space from which sound originates.  
volume | Playback volume.  
  
### Description

Plays an AudioClip at a given position in world space.

This function creates an audio source but automatically disposes of it once
the clip has finished playing.

    
    
    using UnityEngine;  
      
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AudioClip](AudioClip.html) clip; //make sure you assign an actual clip here in the inspector  
      
        void Start()
        {
            [AudioSource.PlayClipAtPoint](AudioSource.PlayClipAtPoint.html)(clip, new [Vector3](Vector3.html)(5, 1, 2));
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

