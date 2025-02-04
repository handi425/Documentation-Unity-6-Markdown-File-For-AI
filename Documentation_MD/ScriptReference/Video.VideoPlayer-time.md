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

#  [VideoPlayer](Video.VideoPlayer.html).time

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

public double time;

### Description

The presentation time of the currently available frame in
[VideoPlayer.texture](Video.VideoPlayer-texture.html) in seconds.

Use `VideoPlayer.time` to achieve the following actions:

  * Start the video at a certain time.
  * Search through a video.
  * Synchronize a part of your clip with another element- for example, with sounds, visual effects or events.

When you set `VideoPlayer.time`, it initiates a seek operation. For example,
if you set `VideoPlayer.time = 10 `, the VideoPlayer:

  1. Starts to move the video towards the 10 second mark.
  2. Fires the [VideoPlayer.seekCompleted](Video.VideoPlayer-seekCompleted.html) event when it reaches 10 seconds.
  3. Prepares the frame at this time for display.
  4. Triggers [VideoPlayer.frameReady](Video.VideoPlayer-frameReady.html) when the frame is prepared and displays the frame.

The `time` value only properly settles when the VideoPlayer displays the
frame.  
  
If you set `time` to another value during this operation, the VideoPlayer
creates a new seek operation and adds it to a queue. The new operation will
start when the previous one completes.  
  
Additional resources: [VideoPlayer.Play](Video.VideoPlayer.Play.html),
[VideoPlayer.texture](Video.VideoPlayer-texture.html).

    
    
    using UnityEngine; 
    using UnityEngine.Video;   
      
    public class TimeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [VideoPlayer](Video.VideoPlayer.html) videoPlayer;  
      
        private void Start()
        {
            // Get the [VideoPlayer](Video.VideoPlayer.html) component from the [GameObject](GameObject.html) that contains this script.  
            videoPlayer = GetComponent<[VideoPlayer](Video.VideoPlayer.html)>();
            // Skip to 10 seconds into the video. 
            videoPlayer.time = 10.0f;
            // Play the video. 
            videoPlayer.Play();
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

