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

#  [AudioSource](AudioSource.html).PlayScheduled

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

public void PlayScheduled(double time);

### Parameters

time | Time in seconds on the absolute time-line that AudioSettings.dspTime refers to for when the sound should start playing.  
---|---  
  
### Description

Plays the [clip](AudioSource-clip.html) at a specific time on the absolute
time-line that AudioSettings.dspTime reads from.

This is the preferred way to stitch AudioClips in music players because it is
independent of the frame rate and gives the audio system enough time to
prepare the playback of the sound to fetch it from media where the opening and
buffering takes a lot of time (streams) without causing sudden CPU spikes.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Basic demonstration of a music system that uses PlayScheduled to preload and sample-accurately
    // stitch two AudioClips in an alternating fashion.  The code assumes that the music pieces are
    // each 16 bars (4 beats / bar) at a tempo of 140 beats per minute.
    // To make it stitch arbitrary clips just replace the line
    //   nextEventTime += (60.0 / bpm) * numBeatsPerSegment
    // by
    //   nextEventTime += clips[flip].length;  
      
    [[RequireComponent](RequireComponent.html)(typeof([AudioSource](AudioSource.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float bpm = 140.0f;
        public int numBeatsPerSegment = 16;
        public [AudioClip](AudioClip.html)[] clips = new [AudioClip](AudioClip.html)[2];  
      
        private double nextEventTime;
        private int flip = 0;
        private [AudioSource](AudioSource.html)[] audioSources = new [AudioSource](AudioSource.html)[2];
        private bool running = false;  
      
        void Start()
        {
            for (int i = 0; i < 2; i++)
            {
                [GameObject](GameObject.html) child = new [GameObject](GameObject.html)("Player");
                child.transform.parent = gameObject.transform;
                audioSources[i] = child.AddComponent<[AudioSource](AudioSource.html)>();
            }  
      
            nextEventTime = [AudioSettings.dspTime](AudioSettings-dspTime.html) + 2.0f;
            running = true;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (!running)
            {
                return;
            }  
      
            double time = [AudioSettings.dspTime](AudioSettings-dspTime.html);  
      
            if (time + 1.0f > nextEventTime)
            {
                // We are now approx. 1 second before the time at which the sound should play,
                // so we will schedule it now in order for the system to have enough time
                // to prepare the playback at the specified time. This may involve opening
                // buffering a streamed file and should therefore take any worst-case delay into account.
                audioSources[flip].clip = clips[flip];
                audioSources[flip].PlayScheduled(nextEventTime);  
      
                [Debug.Log](Debug.Log.html)("Scheduled source " + flip + " to start at time " + nextEventTime);  
      
                // Place the next event 16 beats from here at a rate of 140 beats per minute
                nextEventTime += 60.0f / bpm * numBeatsPerSegment;  
      
                // Flip between two audio sources so that the loading process of one does not interfere with the one that's playing out
                flip = 1 - flip;
            }
        }
    }
    

The example at
[AudioSource.SetScheduledEndTime](AudioSource.SetScheduledEndTime.html) shows
how you can play two audio clips without pops or clicks between the clips. The
approach is to have two AudioSources with clips attached, and queue up each
clip using its AudioSource.  
  
Additional resources:
[SetScheduledStartTime](AudioSource.SetScheduledStartTime.html).

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

