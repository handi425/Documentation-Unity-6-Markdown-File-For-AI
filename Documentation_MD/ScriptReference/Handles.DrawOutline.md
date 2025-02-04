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

#  [Handles](Handles.html).DrawOutline

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

public static void DrawOutline(GameObject[] objects, [Color](Color.html)
parentNodeColor, [Color](Color.html) childNodeColor, float fillOpacity);

## Declaration

public static void DrawOutline(GameObject[] objects, [Color](Color.html)
color, float fillOpacity);

## Declaration

public static void DrawOutline(List<GameObject> objects, [Color](Color.html)
parentNodeColor, [Color](Color.html) childNodeColor, float fillOpacity);

## Declaration

public static void DrawOutline(List<GameObject> objects, [Color](Color.html)
color, float fillOpacity);

## Declaration

public static void DrawOutline(int[] parentRenderers, int[] childRenderers,
[Color](Color.html) parentNodeColor, [Color](Color.html) childNodeColor, float
fillOpacity);

## Declaration

public static void DrawOutline(int[] renderers, [Color](Color.html) color,
float fillOpacity);

## Declaration

public static void DrawOutline(Renderer[] renderers, [Color](Color.html)
parentNodeColor, [Color](Color.html) childNodeColor, float fillOpacity);

## Declaration

public static void DrawOutline(Renderer[] renderers, [Color](Color.html)
color, float fillOpacity);

### Parameters

objects | The GameObjects to outline.  
---|---  
parentNodeColor | The color of the outline of the GameObjects provided explicitly in the `objects` parameter and the `parentRenderers` parameters. The alpha value controls the intensity of the outline.  
childNodeColor | The color of the outline of the GameObjects which are children to the GameObjects in the `objects` parameter. The alpha value controls the intensity of the outline.  
color | The color of the outline for the `objects` and `renderers`.  
parentRenderers | The instance IDs of the first set of Renderers. If you provide GameObjects or Renderers as parameters, these Renderers belong to the GameObjects provided explicitly in the parameters.  
childRenderers | The instance IDs of the second set of Renderers. If you provide GameObjects or Renderers as parameters, these Renderers belong to the child GameObjects of the objects provided in the parameters.  
fillOpacity | The opacity of the Renderers within each outline.  
renderers | The Renderers to outline.  
  
### Description

Draws an outline around the specified GameObjects in the Scene View.

This only applies to GameObjects that have Renderer components. You can only
use this during a [EventType.Repaint](EventType.Repaint.html) event.  
  
Instead of passing in GameObjects or Renderers, you can also use Renderer
[instance IDs](Object.GetInstanceID.html). This improves performance because
Unity doesn't need to get the instance IDs from the GameObjects or Renderers
every time you call this function.  
  
NOTE: Overloads that take GameObject[], Renderer[] or List<GameObject> as
arguments are there for convenience, using them might result in additional
allocations that cause additional garbage collection. To avoid performance or
memory issues, use these overloads only when drawing a relatively small number
of outlines (consider providing renderer instance IDs directly if the number
of outlines exceeds 100).  
  
The alpha values of `parentNodeColor` and `childNodeColor` control the
intensity of the outline, 0 makes it completely transparent and 1 makes it
fully opaque.  
  
The `fillOpacity` controls the weight of the color multiplier for the
Renderer. Higher `fillOpacity` values make the color more intense and leave
the original object less visible.  
  
Additional resources: [Handles.DrawCamera](Handles.DrawCamera.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    namespace [UnityEditor](UnityEditor.html)
    {
        [[CustomEditor](CustomEditor.html)(typeof([GameObject](GameObject.html)))]
        public class CustomInspector : [Editor](Editor.html)
        {
            private [GameObject](GameObject.html)[] objects;  
      
            public void OnEnable()
            {
                // Note: If you use FindGameObjectsWithTag in a Prefab [Stage](SceneManagement.Stage.html) that you opened from a [Scene](SceneManagement.Scene.html),
                // it includes GameObjects from that [Scene](SceneManagement.Scene.html). Instead use:
                // var renderers = [StageUtility.GetCurrentStage](SceneManagement.StageUtility.GetCurrentStage.html)().FindComponentsOfType<[Renderer](Renderer.html)>();
                // to explicitly specify where to get the GameObjects from.
                objects = [GameObject.FindGameObjectsWithTag](GameObject.FindGameObjectsWithTag.html)("Player");  // populate the objects array with game objects
            }  
      
            public void OnSceneGUI()
            {
                // draw the outline with an alpha of 0.5
                if (Event.current.type == [EventType.Repaint](EventType.Repaint.html))
                    [Handles.DrawOutline](Handles.DrawOutline.html)(objects, [Color.yellow](Color-yellow.html), [Color.green](Color-green.html), 0.1f);
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

