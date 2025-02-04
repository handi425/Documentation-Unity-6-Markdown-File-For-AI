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

# IQueryNode

interface in UnityEditor.Search

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

Interface representing a query node.

### Properties

[children](Search.IQueryNode-children.html)| The node's children. Can be null.  
---|---  
[identifier](Search.IQueryNode-identifier.html)| A string representing this
node and its children.  
[leaf](Search.IQueryNode-leaf.html)| True if this node is a leaf. A leaf
doesn't have any children.  
[parent](Search.IQueryNode-parent.html)| Parent of this node. Null if this
node is the root.  
[skipped](Search.IQueryNode-skipped.html)| True if this node is skipped during
evaluation. A node can be skipped if the QueryEngine was configured to skip
unsupported nodes instead of generating errors.  
[token](Search.IQueryNode-token.html)| The token used to build this node.  
[type](Search.IQueryNode-type.html)| The node's type.  
  
### Public Methods

[QueryHashCode](Search.IQueryNode.QueryHashCode.html)| Returns a hashcode for
this node. Multiple nodes can have the same hashcode if they have the same
identifier.  
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

