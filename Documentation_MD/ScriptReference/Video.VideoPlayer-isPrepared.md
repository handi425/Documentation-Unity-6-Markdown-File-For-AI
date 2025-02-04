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

#  [VideoPlayer](Video.VideoPlayer.html).isPrepared

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

public bool isPrepared;

### Description

Returns whether the [VideoPlayer](Video.VideoPlayer.html) has successfully
prepared the content to be played.

A prepared VideoPlayer can play back the content instantly because preliminary
parsing and buffering has been done.  
  
A VideoPlayer starts out as not prepared (`false`). To prepare the
VideoPlayer, you need to use
[VideoPlayer.Prepare](Video.VideoPlayer.Prepare.html). When preparation is
done, the VideoPlayer emits the
[VideoPlayer.prepareCompleted](Video.VideoPlayer-prepareCompleted.html) event,
which sets `isPrepared` to `true`.  
  
The property goes back to `false` when you or the VideoPlayer calls
[VideoPlayer.Stop](Video.VideoPlayer.Stop.html).  
  
If there are preparation failures, this property might never be set to `true`.
In this case, Unity sends an error description through the
[VideoPlayer.errorReceived](Video.VideoPlayer-errorReceived.html) event.  
  
Additional resources: [VideoPlayer.Prepare](Video.VideoPlayer.Prepare.html).

    
    
    using UnityEngine;
    using UnityEngine.Video;
    using System.Collections;  
      
    // In the Inspector of your [GameObject](GameObject.html), attach this script and a [VideoPlayer](Video.VideoPlayer.html) component. 
    // Also, assign a [VideoClip](Video.VideoClip.html) to your [VideoPlayer](Video.VideoPlayer.html) component.  
    // Use this script to prepare a video.    
      
    public class IsPreparedExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public IEnumerator Start()
        {
            [VideoPlayer](Video.VideoPlayer.html) videoPlayer = GetComponent<[VideoPlayer](Video.VideoPlayer.html)>();
            videoPlayer.Prepare();
            // Loops until the video is ready.
            // Then outputs the message to the console when the preparation is done. 
            while (!videoPlayer.isPrepared)
            {
                yield return null;
            }
            [Debug.Log](Debug.Log.html)("Preparation completed!");
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

