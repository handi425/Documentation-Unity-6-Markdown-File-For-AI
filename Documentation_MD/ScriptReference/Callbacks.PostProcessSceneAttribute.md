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

# PostProcessSceneAttribute

class in UnityEditor.Callbacks

/

Inherits from:[CallbackOrderAttribute](CallbackOrderAttribute.html)

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

Add this attribute to a method to get a notification just after building the
Scene.

A method with this attribute will also get called when entering Playmode, when
[SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html) is
called.  
  
`PostProcessSceneAttribute` has an option to provide an order index in the
callback, starting at 0. This is useful if you have more than one
OnPostprocessScene callback, and you would like them to be called in a certain
order. Callbacks are called in order, starting at zero.  
  
**Note:** If there are no new changes to the scene since the previous Player
build, Unity doesn't rebuild the scene but uses cached Player data instead. In
this case the `PostProcessSceneAttribute` callback is not called. To ensure an
unchanged scene rebuilds, you can either mark the scene dirty with
[EditorSceneManager.MarkSceneDirty](SceneManagement.EditorSceneManager.MarkSceneDirty.html)
or clear the build cache with
[BuildOptions.CleanBuildCache](BuildOptions.CleanBuildCache.html).  
  
Additional resources:
[IProcessSceneWithReport](Build.IProcessSceneWithReport.html)

    
    
    // C# example:
    // Automatically creates a game object with a primitive mesh renderer and appropriate collider.
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;  
      
    public class MyScenePostprocessor {
        [[PostProcessSceneAttribute](Callbacks.PostProcessSceneAttribute.html) (2)]
        public static void OnPostprocessScene() {
            [GameObject](GameObject.html) cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            cube.transform.position = new [Vector3](Vector3.html)(0.0f, 0.5f, 0.0f);
        }
    }
    

### Inherited Members

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

