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

#  [AudioListener](AudioListener.html).GetSpectrumData

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

[Switch to Manual](../Manual/class-AudioListener.html "Go to AudioListener
Component in the Manual")

## Declaration

public static void GetSpectrumData(float[] samples, int channel,
[FFTWindow](FFTWindow.html) window);

### Parameters

samples | The array to populate with audio samples. Its length must be a power of 2.  
---|---  
channel | The channel to sample from.  
window | The FFTWindow type to use when sampling.  
  
### Description

Provides a block of the listener (master)'s spectrum data.

The array given in the samples parameter will be filled with the requested
data.  
  
Number of values (the length of the samples array) must be a power of 2. (ie
128/256/512 etc). Min = 64. Max = 8192. Use [window](FFTWindow.html) to reduce
leakage between frequency bins/bands. Note, the more complex window type, the
better the quality, but reduced speed.  
  
This function will use the sampling rate specified in
[AudioSettings.outputSampleRate](AudioSettings-outputSampleRate.html), and NOT
the sampling rate specified for the audio clip.  
  
Additional resources:
[AudioListener.GetOutputData](AudioListener.GetOutputData.html),
[AudioSource.GetSpectrumData](AudioSource.GetSpectrumData.html),
[AudioSource.GetOutputData](AudioSource.GetOutputData.html).

    
    
    using UnityEngine;  
      
    
    [[RequireComponent](RequireComponent.html)(typeof([AudioListener](AudioListener.html)))]
    public class GetSpectrumDataExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            float[] spectrum = new float[256];  
      
            [AudioListener.GetSpectrumData](AudioListener.GetSpectrumData.html)(spectrum, 0, [FFTWindow.Rectangular](FFTWindow.Rectangular.html));  
      
            for (int i = 1; i < spectrum.Length - 1; i++)
            {
                [Debug.DrawLine](Debug.DrawLine.html)(new [Vector3](Vector3.html)(i - 1, spectrum[i] + 10, 0), new [Vector3](Vector3.html)(i, spectrum[i + 1] + 10, 0), [Color.red](Color-red.html));
                [Debug.DrawLine](Debug.DrawLine.html)(new [Vector3](Vector3.html)(i - 1, [Mathf.Log](Mathf.Log.html)(spectrum[i - 1]) + 10, 2), new [Vector3](Vector3.html)(i, [Mathf.Log](Mathf.Log.html)(spectrum[i]) + 10, 2), [Color.cyan](Color-cyan.html));
                [Debug.DrawLine](Debug.DrawLine.html)(new [Vector3](Vector3.html)([Mathf.Log](Mathf.Log.html)(i - 1), spectrum[i - 1] - 10, 1), new [Vector3](Vector3.html)([Mathf.Log](Mathf.Log.html)(i), spectrum[i] - 10, 1), [Color.green](Color-green.html));
                [Debug.DrawLine](Debug.DrawLine.html)(new [Vector3](Vector3.html)([Mathf.Log](Mathf.Log.html)(i - 1), [Mathf.Log](Mathf.Log.html)(spectrum[i - 1]), 3), new [Vector3](Vector3.html)([Mathf.Log](Mathf.Log.html)(i), [Mathf.Log](Mathf.Log.html)(spectrum[i]), 3), [Color.blue](Color-blue.html));
            }
        }
    }
    

* * *

**Obsolete** GetSpectrumData returning a float[] is deprecated, use
GetSpectrumData and pass a pre allocated array instead.

## Declaration

public static float[] GetSpectrumData(int numSamples, int channel,
[FFTWindow](FFTWindow.html) window);

### Parameters

numSamples | Number of values (the length of the samples array). Must be a power of 2. Min = 64. Max = 8192.  
---|---  
channel | The channel to sample from.  
window | The FFTWindow type to use when sampling.  
  
### Description

_Deprecated Version_. Returns a block of the listener (master)'s spectrum
data.

This variation of the function allocates a new array each time it is called.
Use the Non-alloc version instead for better performance.

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

