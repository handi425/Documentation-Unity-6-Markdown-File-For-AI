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

#  [Application](Application.html).backgroundLoadingPriority

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

public static [ThreadPriority](ThreadPriority.html) backgroundLoadingPriority;

### Description

Priority of background loading thread.

Lets you control how long it takes to load data asynchronously vs performance
impact on the game while loading in the background.  
  
Asynchronous load functions that load objects
([Resources.LoadAsync](Resources.LoadAsync.html),
[AssetBundle.LoadAssetAsync](AssetBundle.LoadAssetAsync.html),
AssetBundle.LoadAllAssetAsync), scenes
([SceneManager.LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html))
do data read and deserialization on a separate background loading thread and
object integration on a main thread. _Integration_ depends on an object type
and for textures, meshes means uploading data to the GPU, audio clips prepare
data for playing.  
  
To avoid hiccups we limit _integration_ time on a main thread depending on
[backgroundLoadingPriority](Application-backgroundLoadingPriority.html) value:  
\- [ThreadPriority.Low](ThreadPriority.Low.html) \- 2ms  
\- [ThreadPriority.BelowNormal](ThreadPriority.BelowNormal.html) \- 4ms  
\- [ThreadPriority.Normal](ThreadPriority.Normal.html) \- 10ms  
\- [ThreadPriority.High](ThreadPriority.High.html) \- 50ms  
This is a maximum time all asynchronous operations can spend within a single
frame on a main thread.  
  
Background loading thread uses [backgroundLoadingPriority](Application-
backgroundLoadingPriority.html) directly.  
  
The Profiler marker **Application.Integrate Assets in Background** lets you
optimize background loading.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Example1()
        {
            // Load as much data as possible, as a result frame rate will drop.
            // Good for fast loading when showing progress bars.  
      
            [Application.backgroundLoadingPriority](Application-backgroundLoadingPriority.html) = [ThreadPriority.High](ThreadPriority.High.html);
        }  
      
        void Example2()
        {
            // Load data very slowly and try not to affect performance of the game.
            // Good for loading in the background while the game is playing.  
      
            [Application.backgroundLoadingPriority](Application-backgroundLoadingPriority.html) = [ThreadPriority.Low](ThreadPriority.Low.html);
        }
    }
    

Additional resources: [ThreadPriority](ThreadPriority.html) enum,
[AsyncOperation.priority](AsyncOperation-priority.html).

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

