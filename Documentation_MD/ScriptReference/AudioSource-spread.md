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

#  [AudioSource](AudioSource.html).spread

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

public float spread;

### Description

Sets the spread angle (in degrees) of a 3d stereo or multichannel sound in
speaker space.

0 = all sound channels are located at the same speaker location and is 'mono'.
360 = all subchannels are located at the opposite speaker location to the
speaker location that it should be according to 3D position. Default = 0.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // when any [AudioSource](AudioSource.html) goes trough this transform, it will set it as 'mono'
        // and will restore the value to 3D effect after exiting
        // Make sure the audio source has a collider.
        void OnTriggerEnter([Collider](Collider.html) other)
        {
            [AudioSource](AudioSource.html) audio = other.GetComponent<[AudioSource](AudioSource.html)>();  
      
            if (audio)
            {
                audio.spread = 0;
            }
        }  
      
        void OnTriggerExit([Collider](Collider.html) other)
        {
            [AudioSource](AudioSource.html) audio = other.GetComponent<[AudioSource](AudioSource.html)>();  
      
            if (audio)
            {
                audio.spread = 360;
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

