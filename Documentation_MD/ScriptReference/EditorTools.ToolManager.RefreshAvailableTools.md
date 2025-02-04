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

#  [ToolManager](EditorTools.ToolManager.html).RefreshAvailableTools

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

public static void RefreshAvailableTools();

### Description

Call RefreshAvailableTools to rebuild the contents of the Scene View Tools
Overlay.

This method is useful when a tool can change the value of
[EditorTool.IsAvailable](EditorTools.EditorTool.IsAvailable.html) outside of
selection and tool change events.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;
    using UnityEngine;  
      
    // An example of a tool that may be made available or unavailable in situations other than selection changes.
    [[EditorTool](EditorTools.EditorTool.html)("Conditional [Tool](Tool.html)", typeof([Transform](Transform.html)))]
    class ConditionallyAvailable : [EditorTool](EditorTools.EditorTool.html)
    {
        bool m_IsAvailable;
        void OnEnable() => [EditorApplication.update](EditorApplication-update.html) += UpdateAvailable;
        void OnDisable() => [EditorApplication.update](EditorApplication-update.html) -= UpdateAvailable;  
      
        // This tool is enabled and disabled in 10 second intervals.
        void UpdateAvailable()
        {
            var time = DateTime.Now;  
      
            if (m_IsAvailable != ((time.Second / 10) % 2 == 0))
            {
                m_IsAvailable = !m_IsAvailable;
                // Because the tool is changing availability arbitrarily, it is necessary to manually refresh the UI.
                [ToolManager.RefreshAvailableTools](EditorTools.ToolManager.RefreshAvailableTools.html)();
            }
        }  
      
        // When a tool is available, it is shown in the [Tools](Tools.html) [Overlay](Overlays.Overlay.html). If not available, it is hidden.
        public override bool IsAvailable() => m_IsAvailable;
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

