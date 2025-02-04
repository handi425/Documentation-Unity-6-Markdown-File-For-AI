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

# DrawGizmo Constructor

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

public DrawGizmo([GizmoType](GizmoType.html) gizmo);

### Parameters

gizmo | Flags to denote when the gizmo should be drawn.  
---|---  
  
### Description

Defines when the gizmo should be invoked for drawing.

Additional resources: [GizmoType](GizmoType.html),
[DrawGizmo](DrawGizmo.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Draw an image above the light when the light is not selected
    // The icon has to be stored in Assets/[Gizmos](Gizmos.html)  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draw an image above the light when the light is not selected
        [[DrawGizmo](DrawGizmo.html)([GizmoType.NotInSelectionHierarchy](GizmoType.NotInSelectionHierarchy.html) | [GizmoType.Pickable](GizmoType.Pickable.html))]
        static void drawGizmo1([Light](Light.html) light, [GizmoType](GizmoType.html) gizmoType)
        {
            [Vector3](Vector3.html) position = light.transform.position;  
      
            [Gizmos.DrawIcon](Gizmos.DrawIcon.html)(position + [Vector3.up](Vector3-up.html), "ninja.jpg");
        }  
      
        // Place a red sphere around a selected light.
        // Surround the sphere dark shaded when not selected.
        [[DrawGizmo](DrawGizmo.html)([GizmoType.Selected](GizmoType.Selected.html) | [GizmoType.NonSelected](GizmoType.NonSelected.html))]
        static void drawGizmo2([Light](Light.html) light, [GizmoType](GizmoType.html) gizmoType)
        {
            [Vector3](Vector3.html) position = light.transform.position;  
      
            if ((gizmoType & [GizmoType.Selected](GizmoType.Selected.html)) != 0)
            {
                [Gizmos.color](Gizmos-color.html) = [Color.red](Color-red.html);
            }
            else
            {
                [Gizmos.color](Gizmos-color.html) = [Color.red](Color-red.html) * 0.5f;
            }
            [Gizmos.DrawSphere](Gizmos.DrawSphere.html)(position , 1);
        }
    }
    

* * *

## Declaration

public DrawGizmo([GizmoType](GizmoType.html) gizmo, Type drawnGizmoType);

### Parameters

gizmo | Flags to denote when the gizmo should be drawn.  
---|---  
drawnGizmoType | Type of object for which the gizmo should be drawn.  
  
### Description

Same as above. `drawnGizmoType` determines of what type the object we are
drawing the gizmo of has to be.

If drawnGizmoType is null, the type will be determined from the first
parameter of the draw gizmo method. If drawnGizmoType is not null, it must be
the same type as, or a subtype of, the type of the first parameter.

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

