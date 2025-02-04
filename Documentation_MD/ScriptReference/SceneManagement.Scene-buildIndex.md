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

#  [Scene](SceneManagement.Scene.html).buildIndex

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

public int buildIndex;

### Description

Return the index of the Scene in the Build Settings.

[Scene.buildIndex](SceneManagement.Scene-buildIndex.html) varies from zero to
the number of [Scene](SceneManagement.Scene.html)s in the `Build Settings`
minus one. This is because indexes start at zero, so the first
[Scene](SceneManagement.Scene.html) is at position zero in the
[buildIndex](SceneManagement.Scene-buildIndex.html). For example, five
[Scene](SceneManagement.Scene.html)s in the `Build Settings` have an index
from zero to four.  
  
Unity ignores any numbers in a `Scene` name. For example, if you add a `Scene`
called `scene15` to a list of five [Scene](SceneManagement.Scene.html)s in the
`Build Settings`, Unity gives it a [buildIndex](SceneManagement.Scene-
buildIndex.html) of 5.  
  
A `Scene` that is not added to the `Scenes in Build` window returns a
[buildIndex](SceneManagement.Scene-buildIndex.html) one more than the highest
in the list. For example, if you don’t add a `Scene` to a `Scenes in Build`
window that already has 6 Scenes in it, then
[Scene.buildIndex](SceneManagement.Scene-buildIndex.html) returns 6 as its
index .  
  
If the `Scene` is loaded through an `AssetBundle`,
[Scene.buildIndex](SceneManagement.Scene-buildIndex.html) returns -1.

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    // Show the buildIndex for the current script.
    //
    // The Build [Settings](Rendering.RayTracingAccelerationStructure.Settings.html) window shows 5 added Scenes.  These have buildIndex values from
    // 0 to 4. Each [Scene](SceneManagement.Scene.html) has a version of this script applied.
    //
    // In the Project, create 5 Scenes called scene1, scene2, scene3, scene4 and scene5.
    // In each [Scene](SceneManagement.Scene.html) add an empty [GameObject](GameObject.html) and attach this script to it.
    //
    // Each [Scene](SceneManagement.Scene.html) randomly switches to a different [Scene](SceneManagement.Scene.html) when the button is clicked.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [Scene](SceneManagement.Scene.html) scene;  
      
        void Start()
        {
            scene = [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)();
            [Debug.Log](Debug.Log.html)("Active [Scene](SceneManagement.Scene.html) name is: " + scene.name + "\nActive [Scene](SceneManagement.Scene.html) index: " + scene.buildIndex);
        }  
      
        void OnGUI()
        {
            GUI.skin.button.fontSize = 20;  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 80, 180, 60), "Change from scene " + scene.buildIndex))
            {
                int nextSceneIndex = [Random.Range](Random.Range.html)(0, 4);
                [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)(nextSceneIndex, [LoadSceneMode.Single](SceneManagement.LoadSceneMode.Single.html));
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

