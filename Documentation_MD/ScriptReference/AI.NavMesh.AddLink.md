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

#  [NavMesh](AI.NavMesh.html).AddLink

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

public static [AI.NavMeshLinkInstance](AI.NavMeshLinkInstance.html)
AddLink([AI.NavMeshLinkData](AI.NavMeshLinkData.html) link);

### Parameters

link | Object that describes the properties of the link.  
---|---  
  
### Returns

**NavMeshLinkInstance** Object that identifies the added link.

### Description

Adds a link to the NavMesh. The link is described by the NavMeshLinkData
struct.

Returns an instance identifier for the added link.  
  
The returned instance is valid if the link was successfully added. The
instance can be used to later remove the link using RemoveLink().  
  
**Note:** If the area is set to Not Walkable, or if adding a link would exceed
the maximum number of active links (65535) the link will fail to be added –
and the valid property will be false.  
  
Additional resources: [NavMeshLinkInstance](AI.NavMeshLinkInstance.html),
[RemoveLink](AI.NavMesh.RemoveLink.html).

* * *

## Declaration

public static [AI.NavMeshLinkInstance](AI.NavMeshLinkInstance.html)
AddLink([AI.NavMeshLinkData](AI.NavMeshLinkData.html) link,
[Vector3](Vector3.html) position, [Quaternion](Quaternion.html) rotation);

### Parameters

link | Object that describes the properties of the link.  
---|---  
position | Translate the link to this position.  
rotation | Rotate the link to this orientation.  
  
### Returns

**NavMeshLinkInstance** Object that identifies the added link.

### Description

Adds a link to the NavMesh. The link is described by the NavMeshLinkData
struct.

Returns an instance identifier for the added link.  
  
This function is similar to AddLink above, but the position and rotation
specified is applied to the start and end positions of the link. The rotation
also specifies the local up-axis of the link.  
  
Additional resources: [NavMeshLinkInstance](AI.NavMeshLinkInstance.html),
[RemoveLink](AI.NavMesh.RemoveLink.html).

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

