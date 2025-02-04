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

#  [PlayableDirector](Playables.PlayableDirector.html).paused

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

### Description

Event that is raised when a PlayableDirector component has paused.

Add an event handler, to this event, to receive a notification when a
PlayableDirector is paused. The handler also receives the PlayableDirector
that is paused.  
  
When using [PlayableBehaviour](Playables.PlayableBehaviour.html), this event
is raised before
[PlayableBehaviour.OnBehaviourPause](Playables.PlayableBehaviour.OnBehaviourPause.html).

    
    
    using UnityEngine;
    using UnityEngine.Playables;  
      
    public class PlayableDirectorCallbackExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [PlayableDirector](Playables.PlayableDirector.html) director;  
      
        void OnEnable()
        {
            director.paused += OnPlayableDirectorPaused;
        }  
      
        void OnPlayableDirectorPaused([PlayableDirector](Playables.PlayableDirector.html) aDirector)
        {
            if (director == aDirector)
                [Debug.Log](Debug.Log.html)("[PlayableDirector](Playables.PlayableDirector.html) named " + aDirector.name + " is now paused.");
        }  
      
        void OnDisable()
        {
            director.paused -= OnPlayableDirectorPaused;
        }
    }
    

Additional resources: [PlayableDirector.played](Playables.PlayableDirector-
played.html), [PlayableDirector.stopped](Playables.PlayableDirector-
stopped.html).

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

