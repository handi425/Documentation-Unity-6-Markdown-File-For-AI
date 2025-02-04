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

#  [AudioClip](AudioClip.html).Create

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

public static [AudioClip](AudioClip.html) Create(string name, int
lengthSamples, int channels, int frequency, bool stream);

## Declaration

public static [AudioClip](AudioClip.html) Create(string name, int
lengthSamples, int channels, int frequency, bool stream,
[AudioClip.PCMReaderCallback](AudioClip.PCMReaderCallback.html)
pcmreadercallback);

## Declaration

public static [AudioClip](AudioClip.html) Create(string name, int
lengthSamples, int channels, int frequency, bool stream,
[AudioClip.PCMReaderCallback](AudioClip.PCMReaderCallback.html)
pcmreadercallback,
[AudioClip.PCMSetPositionCallback](AudioClip.PCMSetPositionCallback.html)
pcmsetpositioncallback);

**Obsolete** The _3D argument of AudioClip is deprecated. Use the spatialBlend
property of AudioSource instead to morph between 2D and 3D playback.

## Declaration

public static [AudioClip](AudioClip.html) Create(string name, int
lengthSamples, int channels, int frequency, bool _3D, bool stream);

**Obsolete** The _3D argument of AudioClip is deprecated. Use the spatialBlend
property of AudioSource instead to morph between 2D and 3D playback.

## Declaration

public static [AudioClip](AudioClip.html) Create(string name, int
lengthSamples, int channels, int frequency, bool _3D, bool stream,
[AudioClip.PCMReaderCallback](AudioClip.PCMReaderCallback.html)
pcmreadercallback);

**Obsolete** The _3D argument of AudioClip is deprecated. Use the spatialBlend
property of AudioSource instead to morph between 2D and 3D playback.

## Declaration

public static [AudioClip](AudioClip.html) Create(string name, int
lengthSamples, int channels, int frequency, bool _3D, bool stream,
[AudioClip.PCMReaderCallback](AudioClip.PCMReaderCallback.html)
pcmreadercallback,
[AudioClip.PCMSetPositionCallback](AudioClip.PCMSetPositionCallback.html)
pcmsetpositioncallback);

### Parameters

name | Name of clip.  
---|---  
lengthSamples | Number of sample frames.  
channels | Number of channels per frame.  
frequency | Sample frequency of clip.  
_3D | Audio clip is played back in 3D.  
stream | True if clip is streamed, that is if the pcmreadercallback generates data on the fly.  
pcmreadercallback | This callback is invoked to generate a block of sample data. Non-streamed clips call this only once at creation time while streamed clips call this continuously.  
pcmsetpositioncallback | This callback is invoked whenever the clip loops or changes playback position.  
  
### Returns

**AudioClip** A reference to the created AudioClip.

### Description

Creates a user AudioClip with a name and with the given length in samples,
channels and frequency.

Set your own audio data with SetData. Use the PCMReaderCallback and
PCMSetPositionCallback delegates to get a callback whenever the clip reads
data and changes the position. If stream is true, Unity will on demand read in
small chunks of data. If it's false, all the samples will be read during the
creation.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public int position = 0;
        public int samplerate = 44100;
        public float frequency = 440;  
      
        void Start()
        {
            [AudioClip](AudioClip.html) myClip = [AudioClip.Create](AudioClip.Create.html)("MySinusoid", samplerate * 2, 1, samplerate, true, OnAudioRead, OnAudioSetPosition);
            [AudioSource](AudioSource.html) aud = GetComponent<[AudioSource](AudioSource.html)>();
            aud.clip = myClip;
            aud.Play();
        }  
      
        void OnAudioRead(float[] data)
        {
            int count = 0;
            while (count < data.Length)
            {
                data[count] = [Mathf.Sin](Mathf.Sin.html)(2 * [Mathf.PI](Mathf.PI.html) * frequency * position / samplerate);
                position++;
                count++;
            }
        }  
      
        void OnAudioSetPosition(int newPosition)
        {
            position = newPosition;
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

