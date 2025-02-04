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

# PropertyPathPart

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

A [PropertyPathPart](Unity.Properties.PropertyPathPart.html) represents a
single element of the path.

[PropertyPathPartKind.Name](Unity.Properties.PropertyPathPartKind.Name.html)
-> ".{name}"
[PropertyPathPartKind.Index](Unity.Properties.PropertyPathPartKind.Index.html)
-> "[{index}]"
[PropertyPathPartKind.Key](Unity.Properties.PropertyPathPartKind.Key.html) ->
"[{key}]"

### Properties

[Index](Unity.Properties.PropertyPathPart.Index.html)|  The Index of the part.
This will only be set when using PropertyPathPartKind.Index  
---|---  
[IsIndex](Unity.Properties.PropertyPathPart.IsIndex.html)|  Returns true if
the part is PropertyPathPartKind.Index.  
[IsKey](Unity.Properties.PropertyPathPart.IsKey.html)|  Returns true if the
part is PropertyPathPartKind.Key.  
[IsName](Unity.Properties.PropertyPathPart.IsName.html)|  Returns true if the
part is PropertyPathPartKind.Name.  
[Key](Unity.Properties.PropertyPathPart.Key.html)|  The Key of the part. This
will only be set when using PropertyPathPartKind.Key  
[Kind](Unity.Properties.PropertyPathPart.Kind.html)|  The PropertyPathPartKind
for this path. This determines how algorithms will resolve the path.  
[Name](Unity.Properties.PropertyPathPart.Name.html)|  The Name of the part.
This will only be set when using PropertyPathPartKind.Name  
  
### Constructors

[PropertyPathPart](Unity.Properties.PropertyPathPart-ctor.html)|  Initializes
a new PropertyPathPart with the specified name.  
---|---  
  
### Public Methods

[Equals](Unity.Properties.PropertyPathPart.Equals.html)|  Indicates whether
this instance and a specified object are equal.  
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

