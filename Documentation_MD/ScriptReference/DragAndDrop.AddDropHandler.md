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

#  [DragAndDrop](DragAndDrop.html).AddDropHandler

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

public static void
AddDropHandler([DragAndDrop.ProjectBrowserDropHandler](DragAndDrop.ProjectBrowserDropHandler.html)
handler);

## Declaration

public static void
AddDropHandler([DragAndDrop.SceneDropHandler](DragAndDrop.SceneDropHandler.html)
handler);

## Declaration

public static void
AddDropHandler([DragAndDrop.HierarchyDropHandler](DragAndDrop.HierarchyDropHandler.html)
handler);

## Declaration

public static void
AddDropHandler([DragAndDrop.InspectorDropHandler](DragAndDrop.InspectorDropHandler.html)
handler);

### Parameters

handler | Function to handle drop on the corresponding window.  
---|---  
  
### Description

Allow override of the default behavior for the corresponding window. Multiple
handlers can be registered on the same window. If a handler returns
[DragAndDropVisualMode.None](DragAndDropVisualMode.None.html) the system will
check the next handler. Any other results
([DragAndDropVisualMode.Rejected](DragAndDropVisualMode.Rejected.html) or
others [DragAndDropVisualMode](DragAndDropVisualMode.html)) means this handler
has processed the drop event and no other handler will be called. The last
handler is the default Unity handler.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    static class DragDropSample
    {
        static [DragAndDropVisualMode](DragAndDropVisualMode.html) ProjectHandler(int id, string path, bool perform)
        {
            if (perform)
                [Debug.Log](Debug.Log.html)($"Dropped upon {path} {id}");
            else
                [Debug.Log](Debug.Log.html)($"Dragging upon {path} {id}");
            return [DragAndDropVisualMode.Move](DragAndDropVisualMode.Move.html);
        }  
      
        public static void AddDragProjectHandler()
        {
            // Add the handler
            [DragAndDrop.AddDropHandler](DragAndDrop.AddDropHandler.html)(ProjectHandler);
        }  
      
        public static void RemoveProjectHandler()
        {
            // Remove the handler
            [DragAndDrop.RemoveDropHandler](DragAndDrop.RemoveDropHandler.html)(ProjectHandler);
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

