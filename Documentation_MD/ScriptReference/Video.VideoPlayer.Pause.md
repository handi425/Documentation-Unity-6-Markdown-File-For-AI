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

#  [VideoPlayer](Video.VideoPlayer.html).Pause

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

[ ]()

## Declaration

public void Pause();

### Description

Pauses the playback and leaves the current time intact.

Use this method to pause the playback of a video. This method sets
[VideoPlayer.isPlaying](Video.VideoPlayer-isPlaying.html) to `false`. To play
again, use [VideoPlayer.Play](Video.VideoPlayer.Play.html).  
  
If you pause the video when the VideoPlayer isn't prepared, this method
triggers preparation and shows the first frame of the video.  
  
If you seek through to a different point in the video and then call `Pause()`
before the VideoPlayer finishes preparation, it triggers preparation and shows
the frame that was the seek target. For example, if you set
[VideoPlayer.time](Video.VideoPlayer-time.html) to `10.0f` and then call
`Pause()`, it shows the frame at 10 seconds.  
  
Additional resources: [VideoPlayer.Play](Video.VideoPlayer.Play.html).

    
    
    // In the Inspector of a [GameObject](GameObject.html), attach this script and a [VideoPlayer](Video.VideoPlayer.html) component.   
      
    using UnityEngine;
    using UnityEngine.Video;  
      
    public class PauseExample: [MonoBehaviour](MonoBehaviour.html)
    {
        [VideoPlayer](Video.VideoPlayer.html) videoPlayer;   
      
        void Start()
        {
            // Get the [VideoPlayer](Video.VideoPlayer.html) component from the [GameObject](GameObject.html) with this script attached. 
            videoPlayer = GetComponent<[VideoPlayer](Video.VideoPlayer.html)>();
        }  
      
        private void [Update](PlayerLoop.Update.html)()
        {
            // Press the Spacebar to pause the video if it's playing. 
            if ([Input.GetKeyDown](Input.GetKeyDown.html)("space"))
            {
                // If the [VideoPlayer](Video.VideoPlayer.html) is currently playing a video, pause the video. 
                if (videoPlayer.isPlaying)
                {
                    videoPlayer.Pause(); 
                }
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

