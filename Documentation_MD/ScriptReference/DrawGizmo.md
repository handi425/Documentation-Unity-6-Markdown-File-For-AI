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

# DrawGizmo

class in UnityEditor

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

The DrawGizmo attribute allows you to supply a gizmo renderer for any
[Component](Component.html).

The renderer function must be static, and take two parameters: the object for
which the gizmo is being drawn, and a [GizmoType](GizmoType.html) parameter
which indicates the context in which the gizmo is being drawn.  
  
The renderer function can be defined in any class, including editor scripts.
This allows you to keep your gizmo-drawing code out of your component scripts
so that it is not included in builds.  
  
Additional resources: [GizmoType](GizmoType.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class MyScript : [MonoBehaviour](MonoBehaviour.html)
    {
    }  
      
    // The icon has to be stored in Assets/[Gizmos](Gizmos.html)  
      
    public class MyScriptGizmoDrawer
    {
        [[DrawGizmo](DrawGizmo.html)([GizmoType.Selected](GizmoType.Selected.html) | [GizmoType.Active](GizmoType.Active.html))]
        static void DrawGizmoForMyScript(MyScript scr, [GizmoType](GizmoType.html) gizmoType)
        {
            [Vector3](Vector3.html) position = scr.transform.position;  
      
            if ([Vector3.Distance](Vector3.Distance.html)(position, Camera.current.transform.position) > 10f)
                [Gizmos.DrawIcon](Gizmos.DrawIcon.html)(position, "MyScript Gizmo.tiff");
        }
    }
    

### Constructors

[DrawGizmo](DrawGizmo-ctor.html)| Defines when the gizmo should be invoked for
drawing.  
---|---  
  
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

