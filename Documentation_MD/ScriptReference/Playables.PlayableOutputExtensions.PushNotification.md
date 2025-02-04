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

#
[PlayableOutputExtensions](Playables.PlayableOutputExtensions.html).PushNotification

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

public static void PushNotification(U output,
[Playables.Playable](Playables.Playable.html) origin,
[Playables.INotification](Playables.INotification.html) notification, object
context);

### Parameters

output | The output sending the notification.  
---|---  
origin | The originating playable of the notification.  
notification | The notification to be sent.  
context | Extra information about the state when the notification was fired.  
  
### Description

Queues a notification to be sent through the Playable system.

    
    
    using UnityEngine;
    using UnityEngine.Playables;
    class ExamplePlayableBehaviour : [PlayableBehaviour](Playables.PlayableBehaviour.html)
    {
        private static readonly [Notification](Playables.Notification.html) s_BlendNotification = new [Notification](Playables.Notification.html)("BlendComplete");
        private float m_lastWeight = 0;  
      
        public override void PrepareFrame([Playable](Playables.Playable.html) playable, [FrameData](Playables.FrameData.html) info)
        {
            if (m_lastWeight < 1 && info.effectiveWeight == 1)
            {
                info.output.PushNotification(playable, s_BlendNotification, m_lastWeight);
            }
            m_lastWeight = info.effectiveWeight;
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

