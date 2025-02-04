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

# PropertyPath

struct in Unity.Properties

/

Implemented
in:[UnityEngine.PropertiesModule](UnityEngine.PropertiesModule.html)

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

A [PropertyPath](Unity.Properties.PropertyPath.html) is used to store a
reference to a single property within a tree.

The path is stored as an array of parts and can be easily queried for
algorithms.

### Properties

[IsEmpty](Unity.Properties.PropertyPath.IsEmpty.html)|  Gets if there is any
part contained in the PropertyPath.  
---|---  
[Length](Unity.Properties.PropertyPath.Length.html)|  Gets the number of parts
contained in the PropertyPath.  
[this[int]](Unity.Properties.PropertyPath.Index_operator.html)|  Gets the
PropertyPathPart at the given index.  
  
### Constructors

[PropertyPath](Unity.Properties.PropertyPath-ctor.html)|  Initializes a new
instance of the PropertyPath based on the given property string.  
---|---  
  
### Public Methods

[Equals](Unity.Properties.PropertyPath.Equals.html)|  Indicates whether this
instance and a specified object are equal.  
---|---  
  
### Static Methods

[AppendIndex](Unity.Properties.PropertyPath.AppendIndex.html)|  Returns a new
PropertyPath combining the given PropertyPath and an index-type
PropertyPathPart.  
---|---  
[AppendKey](Unity.Properties.PropertyPath.AppendKey.html)|  Returns a new
PropertyPath combining the given PropertyPath and an key-type
PropertyPathPart.  
[AppendName](Unity.Properties.PropertyPath.AppendName.html)|  Returns a new
PropertyPath combining the given PropertyPath and an name-type
PropertyPathPart.  
[AppendPart](Unity.Properties.PropertyPath.AppendPart.html)|  Returns a new
PropertyPath combining the given PropertyPath and PropertyPathPart.  
[AppendProperty](Unity.Properties.PropertyPath.AppendProperty.html)|  Returns
a new PropertyPath combining the given PropertyPath and a PropertyPathPart
whose type will be based on the property interfaces.  
[Combine](Unity.Properties.PropertyPath.Combine.html)|  Returns a new
PropertyPath combining the parts of the two given PropertyPath.  
[FromIndex](Unity.Properties.PropertyPath.FromIndex.html)|  Returns a new
PropertyPath from the provided index.  
[FromKey](Unity.Properties.PropertyPath.FromKey.html)|  Returns a new
PropertyPath from the provided key.  
[FromName](Unity.Properties.PropertyPath.FromName.html)|  Returns a new
PropertyPath from the provided name.  
[FromPart](Unity.Properties.PropertyPath.FromPart.html)|  Returns a new
PropertyPath from the provided PropertyPathPart.  
[Pop](Unity.Properties.PropertyPath.Pop.html)|  Returns a new PropertyPath
that will not include the last PropertyPathPart.  
[SubPath](Unity.Properties.PropertyPath.SubPath.html)|  Returns a new
PropertyPath containing the PropertyPathPart starting at the given start
index.  
  
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

