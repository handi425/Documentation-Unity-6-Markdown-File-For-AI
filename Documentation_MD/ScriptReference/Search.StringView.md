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

# StringView

struct in UnityEditor.Search

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

Structure that holds a view on a string, with a specified range of
[startIndex, endIndex[.

A [StringView](Search.StringView.html) contains only a reference to the
original string, a start and an end index. It can be used to quickly create
substrings or do any other operations that would return a contiguous subset of
the original string, without actually copying the data.

### Static Properties

[empty](Search.StringView-empty.html)| An empty StringView.  
---|---  
[nil](Search.StringView-nil.html)| A null StringView.  
  
### Properties

[baseString](Search.StringView-baseString.html)| The base string which this
StringView references.  
---|---  
[endIndex](Search.StringView-endIndex.html)| The end index.  
[length](Search.StringView-length.html)| The length of this StringView.  
[startIndex](Search.StringView-startIndex.html)| The start index.  
[this[int]](Search.StringView.Index_operator.html)| Gets the character at a
specified position in the current StringView.  
[valid](Search.StringView-valid.html)| Boolean indicating if the StringView is
valid.  
  
### Constructors

[StringView](Search.StringView-ctor.html)| Constructs a StringView over an
entire string.  
---|---  
  
### Public Methods

[Contains](Search.StringView.Contains.html)| Checks if a character is
contained in the StringView.  
---|---  
[EndsWith](Search.StringView.EndsWith.html)| Checks if the StringView ends
with the character c.  
[Equals](Search.StringView.Equals.html)| Checks if the StringView is equal to
the object.  
[GetEnumerator](Search.StringView.GetEnumerator.html)| Gets a character
enumerator over this StringView.  
[GetHashCode](Search.StringView.GetHashCode.html)| Gets the hashcode of this
StringView.  
[IndexOf](Search.StringView.IndexOf.html)| Returns the index of the first
occurence of another StringView within this one.  
[LastIndexOf](Search.StringView.LastIndexOf.html)| Returns the index of the
last occurence of another StringView within this one.  
[StartsWith](Search.StringView.StartsWith.html)| Checks if the StringView
starts with the character c.  
[Substring](Search.StringView.Substring.html)| Returns a substring of the
current StringView, starting at index start and until the end of the
StringView.  
[ToString](Search.StringView.ToString.html)| Converts the current StringView
into a string.  
[Trim](Search.StringView.Trim.html)| Returns a new StringView in which all
leading and trailing occurrences of a set of specified characters from the
current StringView are removed.  
  
### Operators

[bool](Search.StringView-operator_stringView.html)| Implicit boolean
conversion operator.  
---|---  
[operator !=](Search.StringView-operator_ne.html)| The not equals operator.  
[operator ==](Search.StringView-operator_eq.html)| The equals operator.  
  
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

