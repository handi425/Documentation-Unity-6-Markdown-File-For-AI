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

**Method group is Obsolete**  

#  [EditorUtility](EditorUtility.html).SetSelectedWireframeHidden

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

**Obsolete** Use EditorUtility.SetSelectedRenderState.

## Declaration

public static void SetSelectedWireframeHidden([Renderer](Renderer.html)
renderer, bool enabled);

### Description

Sets whether the selected Renderer's wireframe will be hidden when the
GameObject it is attached to is selected.

![](../StaticFiles/ScriptRefImages/EditorUtilitySetSelectedWireframeHidden.png)  
_Cube with the wireframe hidden/shown._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Shows / hides the wireframe of the objects in the [Scene](SceneManagement.Scene.html).  
      
    class ShowHideWireFrame : [Editor](Editor.html)
    {
        [[MenuItem](MenuItem.html)("Examples/Show WireFrame %s")]
        static void Show()
        {
            foreach ([GameObject](GameObject.html) obj in [Selection.gameObjects](Selection-gameObjects.html))
            {
                [Renderer](Renderer.html) rend = obj.GetComponent<[Renderer](Renderer.html)>();  
      
                if (rend)
                {
                    EditorUtility.SetSelectedWireframeHidden(rend, false);
                }
            }
        }  
      
        [[MenuItem](MenuItem.html)("Examples/Show WireFrame %s", true)]
        static bool CheckShow()
        {
            return [Selection.activeGameObject](Selection-activeGameObject.html) != null;
        }  
      
        [[MenuItem](MenuItem.html)("Examples/Hide WireFrame %h")]
        static void Hide()
        {
            foreach ([GameObject](GameObject.html) obj in [Selection.gameObjects](Selection-gameObjects.html))
            {
                var rend = obj.GetComponent<[Renderer](Renderer.html)>();  
      
                if (rend)
                {
                    EditorUtility.SetSelectedWireframeHidden(rend, true);
                }
            }
        }  
      
        [[MenuItem](MenuItem.html)("Examples/Hide WireFrame %h", true)]
        static bool CheckHide()
        {
            return [Selection.activeGameObject](Selection-activeGameObject.html) != null;
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

