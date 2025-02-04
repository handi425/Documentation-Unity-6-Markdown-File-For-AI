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

#  [AudioSource](AudioSource.html).GetSpectrumData

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

public void GetSpectrumData(float[] samples, int channel,
[FFTWindow](FFTWindow.html) window);

### Parameters

samples | The array to populate with frequency domain representations of audio samples. The array length must be a power of 2 (such as 128, 256, 512). Also, the length must not be less than 64 or greater than 8192.  
---|---  
channel | The channel to sample from.  
window | The FFTWindow type to use when sampling.  
  
### Description

Provides the block of audio frequencies (spectrum data) of the AudioSource
that is currently playing.

This method fills the array you pass as the `samples` parameter with the
spectrum data of the AudioSource.  
  
The frequency domain represents the frequencies and amplitude of an audio
signal. Spectrum data provides the raw frequency domain data of the audio,
which you can use to create a spectrogram to visualize the data.  
  
Audio frequency bands are ranges of sound frequencies that describe different
parts of the audio spectrum (like sub-bass, bass, brilliance). The audio
frequency bands are evenly spaced between 0 to half of the sampling rate.
GetSpectrumData uses the sampling rate from
[AudioSettings.outputSampleRate](AudioSettings-outputSampleRate.html), not the
sampling rate in the audio clip.  
  
Use [window](FFTWindow.html) to reduce leakage or scalloping loss between
audio frequency bins/bands.  
  
**Note:** A more complex window type might be less efficient and worsen
resolution (lobe width).  
  
For related information, refer to
[AudioSource.GetOutputData](AudioSource.GetOutputData.html),
[AudioListener.GetSpectrumData](AudioListener.GetSpectrumData.html),
[AudioListener.GetOutputData](AudioListener.GetOutputData.html).

    
    
    using UnityEngine;  
      
    
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class AudioSourceGetSpectrumDataExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [AudioSource](AudioSource.html) m_MyAudioSource;  
      
        void Start()
        {
            m_MyAudioSource = GetComponent<[AudioSource](AudioSource.html)>();
        }
        
        void [Update](PlayerLoop.Update.html)()
        {
            float[] spectrum = new float[256];  
      
            m_MyAudioSource.GetSpectrumData(spectrum, 0, [FFTWindow.Rectangular](FFTWindow.Rectangular.html));  
      
            // Loop through the populated array
            // Start the loop from 1 and to 1 less than the length, so the loop can draw lines between adjacent bins.   
      
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

public float[] GetSpectrumData(int numSamples, int channel,
[FFTWindow](FFTWindow.html) window);

### Parameters

numSamples | The number of samples to retrieve. Must be a power of 2.  
---|---  
channel | The channel to sample from.  
window | The FFTWindow type to use when sampling.  
  
### Returns

**float[]** Returns a block of the currently playing source's spectrum data.

### Description

This version of GetSpectrumData is obsolete.

This version of GetSpectrumData is obsolete. Use the other version of
GetSpectrumData instead.  
  
This variation of the function allocates a new array each time it is called.
Use the other version instead for better performance.  
  
Number of values (numSamples) must be a power of 2. (ie 128/256/512 etc). Min
= 64. Max = 8192. Use [window](FFTWindow.html) to reduce leakage between
frequency bins/bands. Note, the more complex window type, the better the
quality, but reduced speed.

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

