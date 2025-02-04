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

# HierarchySearchQueryDescriptor

class in Unity.Hierarchy

/

Implemented
in:[UnityEngine.HierarchyCoreModule](UnityEngine.HierarchyCoreModule.html)

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

Encapsulates all the query filters and text values that are used to filter a
hierarchy.

### Static Properties

[Empty](Unity.Hierarchy.HierarchySearchQueryDescriptor.Empty.html)|  The
default empty query.  
---|---  
[InvalidQuery](Unity.Hierarchy.HierarchySearchQueryDescriptor.InvalidQuery.html)|
The default invalid query.  
  
### Properties

[Filters](Unity.Hierarchy.HierarchySearchQueryDescriptor.Filters.html)|  User-
defined filters. Filters are in this form [filterName][operator][filterValue].
For example: t:Light. Each of these filters can be used by a NodeHandler to
filter according to domain-specific characteristics.  
---|---  
[Invalid](Unity.Hierarchy.HierarchySearchQueryDescriptor.Invalid.html)|
Whether the query invalid. An invalid query yields no node.  
[IsEmpty](Unity.Hierarchy.HierarchySearchQueryDescriptor.IsEmpty.html)|
Whether the query is empty.  
[IsSystemOnlyQuery](Unity.Hierarchy.HierarchySearchQueryDescriptor.IsSystemOnlyQuery.html)|
Whether the query uses system filters. This means NodeHandlers won't be called
for filtering.  
[IsValid](Unity.Hierarchy.HierarchySearchQueryDescriptor.IsValid.html)|
Whether the query is valid.  
[Strict](Unity.Hierarchy.HierarchySearchQueryDescriptor.Strict.html)|  Whether
the query is evaluated strictly. This means that if any filters are invalid,
then the whole query is invalid.  
[SystemFilters](Unity.Hierarchy.HierarchySearchQueryDescriptor.SystemFilters.html)|
The filters used by the hierarchy. Filters are in this form:
[filterName][operator][filterValue]. For example: nodetype:gameobject. These
filters are global to all NodeHandlers.  
[TextValues](Unity.Hierarchy.HierarchySearchQueryDescriptor.TextValues.html)|
All textual values. For example: "cube"  
  
### Constructors

[HierarchySearchQueryDescriptor](Unity.Hierarchy.HierarchySearchQueryDescriptor-
ctor.html)|  The constructor for a query.  
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

