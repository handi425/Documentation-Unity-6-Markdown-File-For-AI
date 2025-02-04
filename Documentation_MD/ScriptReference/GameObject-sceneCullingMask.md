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

#  [GameObject](GameObject.html).sceneCullingMask

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

[Switch to Manual](../Manual/class-GameObject.html "Go to GameObject Component
in the Manual")

public ulong sceneCullingMask;

### Description

The Scene culling mask defined for the GameObject. (Read Only)

Unity uses [SceneCullingMasks](SceneManagement.SceneCullingMasks.html) to
determine which scene to render the GameObject in. The `sceneCullingMask` is a
bitfield stored as an unsigned 64-bit integer
[ulong](https://learn.microsoft.com/en-us/dotnet/csharp/language-
reference/builtin-types/integral-numeric-types). Cameras only render an object
in a scene if the bits set on the Scene's mask (retrievable
with[EditorSceneManager.GetSceneCullingMask](SceneManagement.EditorSceneManager.GetSceneCullingMask.html))
match those in the object's `sceneCullingMask`.

    
    
    using UnityEngine;
    using UnityEditor.SceneManagement;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        
        void Start()
        {
            //Check if gameObject is visible in scene
            if(gameObject.sceneCullingMask == [EditorSceneManager.GetSceneCullingMask](SceneManagement.EditorSceneManager.GetSceneCullingMask.html)(gameObject.scene))
            {
                [Debug.Log](Debug.Log.html)("Object is visible");
            }
            else
            {
                [Debug.Log](Debug.Log.html)("Object is not visible");
            }
        }
    }
    

Additional resources:
[SceneCullingMasks](SceneManagement.SceneCullingMasks.html),
[Camera.overrideSceneCullingMask](Camera-overrideSceneCullingMask.html),
[EditorSceneManager.SetSceneCullingMask](SceneManagement.EditorSceneManager.SetSceneCullingMask.html)

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

