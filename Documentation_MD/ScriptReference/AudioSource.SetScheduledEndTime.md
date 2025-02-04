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

#  [AudioSource](AudioSource.html).SetScheduledEndTime

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

public void SetScheduledEndTime(double time);

### Parameters

time | Time in seconds.  
---|---  
  
### Description

Changes the time at which a sound that has already been scheduled to play will
end. Notice that depending on the timing not all rescheduling requests can be
fulfilled.

Note that the time specified is still a time on the absolute time-line,
meaning that the sound will stop when reaching that time, regardless of when
it was started. So if you have a 5 second long sound and want it to play at
time T and stop after 3 seconds (i.e. silencing the last 2 seconds of the
sound), you need to specify the end time to be T+3. This function is useful in
music systems to overcome the discontinuities in signals that frame-based
lossy codecs cause.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // While this may seem unnecessarily complicated to do this in the case of uncompressed sounds, you can now use
    // the SavWav code from https://gist.github.com/2317063 to save the generated clips into new assets,
    // run the program once with a specified sourceClip and the script will generate "cut1.wav" and "cut2.wav".
    // These can now be imported into Unity as assets and changed to compressed sounds.
    // Since psychoacoustic compression severely alters the waveforms and frequency content of sounds and
    // furthermore operates in a block-based fashion, it would cause very noticeable pops and clicks if we didn't
    // have the sound data after and before the cut point. By having it, even though we are not playing it, the decoder is "warmed up",
    // i.e. it has matching frequency content before and after the transition, so at least the
    // frequency spectrum will be more or less the same before and after the transition and so the click will be less audible
    // than if we had just cut up the sound without the 0.2s overlap regions.
    // This method may also be combined with cross-fading in order to further smoothen out any remaining artifacts.
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [AudioClip](AudioClip.html) sourceClip;
        private [AudioSource](AudioSource.html) audio1;
        private [AudioSource](AudioSource.html) audio2;
        private [AudioClip](AudioClip.html) cutClip1;
        private [AudioClip](AudioClip.html) cutClip2;
        private float overlap = 0.2F;
        private int len1 = 0;
        private int len2 = 0;
        void Start()
        {
            [GameObject](GameObject.html) child;
            child = new [GameObject](GameObject.html)("Player1");
            child.transform.parent = gameObject.transform;
            audio1 = child.AddComponent<[AudioSource](AudioSource.html)>();
            child = new [GameObject](GameObject.html)("Player2");
            child.transform.parent = gameObject.transform;
            audio2 = child.AddComponent<[AudioSource](AudioSource.html)>();
            int overlapSamples;
            if (sourceClip != null)
            {
                len1 = sourceClip.samples / 2;
                len2 = sourceClip.samples - len1;
                overlapSamples = (int)(overlap * sourceClip.frequency);
                cutClip1 = [AudioClip.Create](AudioClip.Create.html)("cut1", len1 + overlapSamples, sourceClip.channels, sourceClip.frequency, false, false);
                cutClip2 = [AudioClip.Create](AudioClip.Create.html)("cut2", len2 + overlapSamples, sourceClip.channels, sourceClip.frequency, false, false);
                float[] smp1 = new float[(len1 + overlapSamples) * sourceClip.channels];
                float[] smp2 = new float[(len2 + overlapSamples) * sourceClip.channels];
                sourceClip.GetData(smp1, 0);
                sourceClip.GetData(smp2, len1 - overlapSamples);
                cutClip1.SetData(smp1, 0);
                cutClip2.SetData(smp2, 0);
            }
            else
            {
                overlapSamples = (int)overlap * cutClip1.frequency;
                len1 = cutClip1.samples - overlapSamples;
                len2 = cutClip2.samples - overlapSamples;
            }
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 50, 230, 40), "Trigger source"))
                audio1.PlayOneShot(sourceClip);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 100, 230, 40), "Trigger cut 1"))
                audio1.PlayOneShot(cutClip1);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 150, 230, 40), "Trigger cut 2"))
                audio1.PlayOneShot(cutClip2);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 200, 230, 40), "Play stitched"))
            {
                audio1.clip = cutClip1;
                audio2.clip = cutClip2;
                double t0 = [AudioSettings.dspTime](AudioSettings-dspTime.html) + 3.0F;
                double clipTime1 = len1;
                clipTime1 /= cutClip1.frequency;
                audio1.PlayScheduled(t0);
                audio1.SetScheduledEndTime(t0 + clipTime1);
                [Debug.Log](Debug.Log.html)("t0 = " + t0 + ", clipTime1 = " + clipTime1 + ", cutClip1.frequency = " + cutClip1.frequency);
                [Debug.Log](Debug.Log.html)("cutClip2.frequency = " + cutClip2.frequency + ", samplerate = " + [AudioSettings.outputSampleRate](AudioSettings-outputSampleRate.html));
                audio2.PlayScheduled(t0 + clipTime1);
                audio2.time = overlap;
            }
        }
    }
    

**Note:** If possible create clips that overlap, and use the scheduled end
time for the first, and [AudioSource.time](AudioSource-time.html) for the
second to trim out the overlapped part, as the example above shows.

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

