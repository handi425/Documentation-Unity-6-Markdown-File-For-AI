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

# DragAndDrop

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

Editor drag & drop operations.

### Static Properties

[activeControlID](DragAndDrop-activeControlID.html)| Get or set ID of
currently active drag and drop control.  
---|---  
[objectReferences](DragAndDrop-objectReferences.html)| References to objects
being dragged.  
[paths](DragAndDrop-paths.html)| The file names being dragged.  
[visualMode](DragAndDrop-visualMode.html)| The visual indication of the drag.  
  
### Static Methods

[AcceptDrag](DragAndDrop.AcceptDrag.html)| Accept a drag operation.  
---|---  
[AddDropHandler](DragAndDrop.AddDropHandler.html)| Allow override of the
default behavior for the corresponding window. Multiple handlers can be
registered on the same window. If a handler returns DragAndDropVisualMode.None
the system will check the next handler. Any other results
(DragAndDropVisualMode.Rejected or others DragAndDropVisualMode) means this
handler has processed the drop event and no other handler will be called. The
last handler is the default Unity handler.  
[GetGenericData](DragAndDrop.GetGenericData.html)| Get data associated with
current drag and drop operation.  
[HasHandler](DragAndDrop.HasHandler.html)| Check if the handler is already
registered for the destination window ID.  
[PrepareStartDrag](DragAndDrop.PrepareStartDrag.html)| Clears drag & drop
data.  
[RemoveDropHandler](DragAndDrop.RemoveDropHandler.html)| Unregister a specific
Drop Handler from a Window Drop Target.  
[SetGenericData](DragAndDrop.SetGenericData.html)| Set data associated with
current drag and drop operation.  
[StartDrag](DragAndDrop.StartDrag.html)| Start a drag operation.  
  
### Delegates

[HierarchyDropHandler](DragAndDrop.HierarchyDropHandler.html)| Handler for the
Hierarchy.  
---|---  
[InspectorDropHandler](DragAndDrop.InspectorDropHandler.html)| Handler for the
Inspector.  
[ProjectBrowserDropHandler](DragAndDrop.ProjectBrowserDropHandler.html)|
Handler for the Project.  
[SceneDropHandler](DragAndDrop.SceneDropHandler.html)| Handler for the Scene.  
  
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

