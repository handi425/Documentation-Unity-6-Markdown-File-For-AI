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

# PropertyName

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Represents a string as an int for efficient lookup and comparison. Use this
for common PropertyNames.  
  
Internally stores just an int to represent the string. A PropertyName can be
created from a string but can not be converted back to a string. The same
string always results in the same int representing that string. Thus this is a
very efficient string representation in both memory and speed when all you
need is comparison.  
  
PropertyName is serializable.  
  
ToString() is only implemented for debugging purposes in the editor it returns
"theName:3737" in the player it returns "Unknown:3737".

### Constructors

[PropertyName](PropertyName-ctor.html)| Initializes the PropertyName using a
string.  
---|---  
  
### Public Methods

[Equals](PropertyName.Equals.html)| Determines whether this instance and a
specified object, which must also be a PropertyName object, have the same
value.  
---|---  
[GetHashCode](PropertyName.GetHashCode.html)| Returns the hash code for this
PropertyName.  
[ToString](PropertyName.ToString.html)| For debugging purposes only. Returns
the string value representing the string in the Editor. Returns
"UnityEngine.PropertyName" in the player.  
  
### Static Methods

[IsNullOrEmpty](PropertyName.IsNullOrEmpty.html)| Indicates whether the
specified PropertyName is an Empty string.  
---|---  
  
### Operators

[operator !=](PropertyName-operator_ne.html)| Determines whether two specified
PropertyName have a different string value.  
---|---  
[operator ==](PropertyName-operator_eq.html)| Determines whether two specified
PropertyName have the same string value. Because two PropertyNames initialized
with the same string value always have the same name index, we can simply
perform a comparison of two ints to find out if the string value equals.  
[PropertyName](PropertyName-operator_string.html)| Converts the string passed
into a PropertyName. Additional resources: PropertyName.ctor(System.String).  
  
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

