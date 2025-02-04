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

#  [ToolManager](EditorTools.ToolManager.html).SetActiveTool

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

public static void SetActiveTool();

## Declaration

public static void SetActiveTool(Type type);

## Declaration

public static void
SetActiveTool([EditorTools.EditorTool](EditorTools.EditorTool.html) tool);

### Parameters

type | The [EditorTool](EditorTools.EditorTool.html) type to set as the active tool.  
---|---  
tool | The [EditorTool](EditorTools.EditorTool.html) instance to set as the active tool.  
  
### Description

Sets the active [EditorTool](EditorTools.EditorTool.html).

To set a built-in tool, such as Move, Rotate, or Scale, to active, use
[Tools.current](Tools-current.html) instead.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;
    using UnityEngine;
    
    class ToolToSetActive : [EditorTool](EditorTools.EditorTool.html)
    {
        [[MenuItem](MenuItem.html)("[Tools](Tools.html)/Set Active [Tool](Tool.html) Type")]
        static void SetActiveToolExample()
        {
            [ToolManager.SetActiveTool](EditorTools.ToolManager.SetActiveTool.html)<ToolToSetActive>();
        }
    
        [Vector3](Vector3.html) m_Position;
    
        public override void OnToolGUI([EditorWindow](EditorWindow.html) window)
        {
            m_Position = [Handles.PositionHandle](Handles.PositionHandle.html)(m_Position, [Quaternion.identity](Quaternion-identity.html));
            [Debug.Log](Debug.Log.html)(m_Position);
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

