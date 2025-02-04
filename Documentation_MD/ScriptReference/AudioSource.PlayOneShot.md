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

#  [AudioSource](AudioSource.html).PlayOneShot

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

public void PlayOneShot([AudioClip](AudioClip.html) clip, float volumeScale =
1.0F);

### Parameters

clip | The clip being played.  
---|---  
volumeScale | The scale of the volume. Unity automatically clamps negative scales to zero. Note: Scales larger than one might cause clipping.  
  
### Description

Plays an [AudioClip](AudioClip.html), and scales the
[AudioSource](AudioSource.html) volume by volumeScale.

[AudioSource.PlayOneShot](AudioSource.PlayOneShot.html) does not cancel clips
that are already being played by
[AudioSource.PlayOneShot](AudioSource.PlayOneShot.html) and
[AudioSource.Play](AudioSource.Play.html). For more information on how this
method differs from [AudioSource.Play](AudioSource.Play.html), see
[AudioSource](AudioSource.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AudioClip](AudioClip.html) impact;
        [AudioSource](AudioSource.html) audioSource;  
      
        void Start()
        {
            audioSource = GetComponent<[AudioSource](AudioSource.html)>();
        }  
      
        void OnCollisionEnter()
        {
            audioSource.PlayOneShot(impact, 0.7F);
        }
    }
    

Additional resources: [AudioSource.Play](AudioSource.Play.html).

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

