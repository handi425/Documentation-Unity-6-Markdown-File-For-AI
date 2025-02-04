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

#  [AudioClip](AudioClip.html).SetData

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

[Switch to Manual](../Manual/class-AudioClip.html "Go to AudioClip Component
in the Manual")

## Declaration

public bool SetData(ReadOnlySpan<float> data, int offsetSamples);

## Declaration

public bool SetData(float[] data, int offsetSamples);

### Description

Set sample data in a clip.

The samples should be float values ranging from -1.0f to 1.0f. Exceeding these
limits causes artifacts and undefined behaviour. The sample count is
determined by the length of the ReadOnlySpan or float array. Use the
offsetSamples parameter to write into an arbitrary position in the clip. If
the length from the offset is longer than the clip length, the write will wrap
around and write the remaining samples from the start of the clip.  
  
With compressed audio files, the sample data can only be set when the _Load
Type_ is set to _Decompress on Load_ in the [Audio Clip](../Manual/class-
AudioClip.html) importer.  
  
For best performance, the Span version is preferred as it does not require
allocating managed memory.

    
    
    using UnityEngine;
    using Unity.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Read all the samples from the clip and halve the gain
        void Start()
        {
            [AudioSource](AudioSource.html) audioSource = GetComponent<[AudioSource](AudioSource.html)>();
            var numSamples = audioSource.clip.samples * audioSource.clip.channels;
            var samples = new NativeArray<float>(numSamples, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            audioSource.clip.GetData(samples, 0);  
      
            for (int i = 0; i < samples.Length; ++i)
            {
                samples[i] = samples[i] * 0.5f;
            }  
      
            audioSource.clip.SetData(samples, 0);
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

