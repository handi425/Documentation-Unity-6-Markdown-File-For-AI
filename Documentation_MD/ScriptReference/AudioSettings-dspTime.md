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

#  [AudioSettings](AudioSettings.html).dspTime

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

[Switch to Manual](../Manual/class-AudioSettings.html "Go to AudioSettings
Component in the Manual")

public static double dspTime;

### Description

Returns the current time of the audio system.

This is a value specified in seconds and based on the actual number of samples
the audio system processes and is therefore much more precise than the time
obtained via the [Time.time](Time-time.html) property.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // The code example shows how to implement a metronome that procedurally generates the click sounds via the OnAudioFilterRead callback.
    // While the game is paused or suspended, this time will not be updated and sounds playing will be paused. Therefore developers of music scheduling routines do not have to do any rescheduling after the app is unpaused  
      
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public double bpm = 140.0F;
        public float gain = 0.5F;
        public int signatureHi = 4;
        public int signatureLo = 4;
        private double nextTick = 0.0F;
        private float amp = 0.0F;
        private float phase = 0.0F;
        private double sampleRate = 0.0F;
        private int accent;
        private bool running = false;
        void Start()
        {
            accent = signatureHi;
            double startTick = [AudioSettings.dspTime](AudioSettings-dspTime.html);
            sampleRate = [AudioSettings.outputSampleRate](AudioSettings-outputSampleRate.html);
            nextTick = startTick * sampleRate;
            running = true;
        }  
      
        void OnAudioFilterRead(float[] data, int channels)
        {
            if (!running)
                return;  
      
            double samplesPerTick = sampleRate * 60.0F / bpm * 4.0F / signatureLo;
            double sample = [AudioSettings.dspTime](AudioSettings-dspTime.html) * sampleRate;
            int dataLen = data.Length / channels;
            int n = 0;
            while (n < dataLen)
            {
                float x = gain * amp * [Mathf.Sin](Mathf.Sin.html)(phase);
                int i = 0;
                while (i < channels)
                {
                    data[n * channels + i] += x;
                    i++;
                }
                while (sample + n >= nextTick)
                {
                    nextTick += samplesPerTick;
                    amp = 1.0F;
                    if (++accent > signatureHi)
                    {
                        accent = 1;
                        amp *= 2.0F;
                    }
                    [Debug.Log](Debug.Log.html)("Tick: " + accent + "/" + signatureHi);
                }
                phase += amp * 0.3F;
                amp *= 0.993F;
                n++;
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

