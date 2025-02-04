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

# ObjectSelectorSearchContext

class in UnityEditor.SearchService

Leave feedback

  

Implements interfaces:[ISearchContext](SearchService.ISearchContext.html)

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

A search context implementation for ObjectSelector search engines. All methods
that are called on an ObjectSelector search engine, and expect a
[ISearchContext](SearchService.ISearchContext.html), receive an object of this
type.

### Properties

[allowedInstanceIds](SearchService.ObjectSelectorSearchContext-
allowedInstanceIds.html)| IEnumerable of integers that contains the
instanceIds of objects that the search can include in its results.  
---|---  
[currentObject](SearchService.ObjectSelectorSearchContext-currentObject.html)|
Identifies the currently selected object.  
[editedObjects](SearchService.ObjectSelectorSearchContext-editedObjects.html)|
When the object selector is opened from an Inspector, this property indicates
which objects are currently being edited.  
[endSessionModes](SearchService.ObjectSelectorSearchContext-
endSessionModes.html)| Flags describing the different modes that EndSession is
in.  
[engineScope](SearchService.ObjectSelectorSearchContext-engineScope.html)| An
enum that identifies the scope of the current search. This property is
automatically set to SearchService.ObjectSelector.EngineScope.  
[guid](SearchService.ObjectSelectorSearchContext-guid.html)| A unique
identifier for this search context.  
[requiredTypeNames](SearchService.ObjectSelectorSearchContext-
requiredTypeNames.html)| An IEnumerable of strings that contains the type name
constraints for this search.  
[requiredTypes](SearchService.ObjectSelectorSearchContext-requiredTypes.html)|
An IEnumerable of types that contains the type constraints for this search.  
[visibleObjects](SearchService.ObjectSelectorSearchContext-
visibleObjects.html)| Indicates which categories of objects are visible in the
window. For example, GameObjects, Assets, or both.  
  
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

