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

#  [Microphone](Microphone.html).Start

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

[Switch to Manual](../Manual/class-Microphone.html "Go to Microphone Component
in the Manual")

## Declaration

public static [AudioClip](AudioClip.html) Start(string deviceName, bool loop,
int lengthSec, int frequency);

### Parameters

deviceName | The name of the device.  
---|---  
loop | Indicates whether the recording should continue recording if lengthSec is reached, and wrap around and record from the beginning of the AudioClip.  
lengthSec | Is the length of the AudioClip produced by the recording.  
frequency | The sample rate of the AudioClip produced by the recording.  
  
### Returns

**AudioClip** The function returns null if the recording fails to start.

### Description

Start Recording with device.

If you pass a null or empty string for the device name then the default
microphone is used. You can get a list of available microphone devices from
the [devices](Microphone-devices.html) property and the range of sample rates
supported by a microphone from the
[GetDeviceCaps](Microphone.GetDeviceCaps.html) property.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Start recording with built-in [Microphone](Microphone.html) and play the recorded audio right away
        void Start()
        {
            [AudioSource](AudioSource.html) audioSource = GetComponent<[AudioSource](AudioSource.html)>();
            audioSource.clip = [Microphone.Start](Microphone.Start.html)("Built-in [Microphone](Microphone.html)", true, 10, 44100);
            audioSource.Play();
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

