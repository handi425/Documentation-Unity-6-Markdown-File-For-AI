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

# BaseBlock

class in Unity.Android.Gradle

/

Inherits
from:[Unity.Android.Gradle.BaseElement](Unity.Android.Gradle.BaseElement.html)

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

Abstract base class for all existing block elements.

Empty blocks don't appear in the resulting file. A block is empty if it has no
children and has no raw value set.

### Constructors

[BaseBlock](Unity.Android.Gradle.BaseBlock-ctor.html)| Element constructor.  
---|---  
  
### Public Methods

[AddElement](Unity.Android.Gradle.BaseBlock.AddElement.html)| Adds a new
element as a child.  
---|---  
[Clear](Unity.Android.Gradle.BaseBlock.Clear.html)| Clears the content of this
element.  
[GetElement](Unity.Android.Gradle.BaseBlock.GetElement.html)| Gets an element
by ID.  
[GetElements](Unity.Android.Gradle.BaseBlock.GetElements.html)| Gets all
custom child elements.  
[GetName](Unity.Android.Gradle.BaseBlock.GetName.html)| Gets the name of the
block. In some cases, the name is the signature of the function.  
[GetRaw](Unity.Android.Gradle.BaseBlock.GetRaw.html)| Gets the raw value of
this block.  
[GetUniqueName](Unity.Android.Gradle.BaseBlock.GetUniqueName.html)| Gets the
unique name of the element.  
[RemoveElement](Unity.Android.Gradle.BaseBlock.RemoveElement.html)| Removes a
child element by id.  
[SetRaw](Unity.Android.Gradle.BaseBlock.SetRaw.html)| Sets a raw string value
to this block.  
[ToString](Unity.Android.Gradle.BaseBlock.ToString.html)| Gets a serialized
value from this block.  
  
### Inherited Members

### Public Methods

[AddElementDependencies](Unity.Android.Gradle.BaseElement.AddElementDependencies.html)|
Adds a list of dependencies by ID to this element.  
---|---  
[AddElementDependency](Unity.Android.Gradle.BaseElement.AddElementDependency.html)|
Adds a dependency to this element.  
[GetElementDependenciesIDs](Unity.Android.Gradle.BaseElement.GetElementDependenciesIDs.html)|
Gets a read-only list of element IDs that this element depends on.  
[GetID](Unity.Android.Gradle.BaseElement.GetID.html)| Gets the unique ID of
this element.  
[Remove](Unity.Android.Gradle.BaseElement.Remove.html)| Removes this element
from the file.  
[RemoveAllElementDependencies](Unity.Android.Gradle.BaseElement.RemoveAllElementDependencies.html)|
Remove all element dependencies.  
[RemoveElementDependency](Unity.Android.Gradle.BaseElement.RemoveElementDependency.html)|
Remove an element dependency.  
[RemoveElementDependencyById](Unity.Android.Gradle.BaseElement.RemoveElementDependencyById.html)|
Remove an element dependency by ID.  
[ResolveConflict](Unity.Android.Gradle.BaseElement.ResolveConflict.html)|
Resolve a conflict if another script has already modified the element.  
  
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

