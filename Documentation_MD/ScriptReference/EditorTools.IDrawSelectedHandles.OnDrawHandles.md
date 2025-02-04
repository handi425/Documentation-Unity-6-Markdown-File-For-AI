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

#  [IDrawSelectedHandles](EditorTools.IDrawSelectedHandles.html).OnDrawHandles

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

public void OnDrawHandles();

### Description

Implement this method to draw non-interactive handles when a custom editor
tool is available.

This method is called when a custom editor tool is available for the current
selection. Use this method to draw information in the SceneView. A custom
editor tool is an
[EditorTool](EditorTools.IDrawSelectedHandles.EditorTool.html) with a target
type specified by the
[EditorToolAttribute](EditorTools.IDrawSelectedHandles.EditorToolAttribute.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;  
      
    [[EditorTool](EditorTools.EditorTool.html)("[Light](Light.html) [Tool](Tool.html)", typeof([Light](Light.html)))]
    public class CustomEditorLightTool : [EditorTool](EditorTools.EditorTool.html), [IDrawSelectedHandles](EditorTools.IDrawSelectedHandles.html)
    {
        // OnToolGUI is called when the tool is active. Interactive handles belong here.
        public override void OnToolGUI([EditorWindow](EditorWindow.html) window)
        {
            var position = [Tools.handlePosition](Tools-handlePosition.html);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();  
      
            var result = [Handles.PositionHandle](Handles.PositionHandle.html)(position, [Quaternion.identity](Quaternion-identity.html));  
      
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                var delta = result - position;  
      
                [Undo.RecordObjects](Undo.RecordObjects.html)([Selection.transforms](Selection-transforms.html), "Move Lights");  
      
                foreach (var light in targets)
                    (([Light](Light.html))light).transform.position += delta;
            }
        }  
      
        // OnDrawHandles is called when a custom editor tool is available for the current selection. Use this to draw
        // information in the [SceneView](SceneView.html) when any object matching the target type is selected.
        public void OnDrawHandles()
        {
            foreach (var light in targets)
            {
                // If the [Light](Light.html) [Tool](Tool.html) is active, draw a green radius handle. If it is not active, make the radius blue.
                [Handles.color](Handles-color.html) = EditorTools.IsActiveTool(this) ? [Color.green](Color-green.html) : [Color.blue](Color-blue.html);
                [Handles.RadiusHandle](Handles.RadiusHandle.html)([Quaternion.identity](Quaternion-identity.html), (([Light](Light.html))light).transform.position, 2f);
                [Handles.color](Handles-color.html) = [Color.white](Color-white.html);
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

