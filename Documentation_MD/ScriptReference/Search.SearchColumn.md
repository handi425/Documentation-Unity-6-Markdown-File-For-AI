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

# SearchColumn

class in UnityEditor.Search

Leave feedback

  

Implements
interfaces:[ISerializationCallbackReceiver](ISerializationCallbackReceiver.html)

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

Search columns are used to display additional information in the Search Table
view.

See [SearchProvider.fetchColumns](Search.SearchProvider-fetchColumns.html) and
[SearchColumnProviderAttribute](Search.SearchColumnProviderAttribute.html) for
some examples.

### Properties

[binder](Search.SearchColumn-binder.html)| If defined, the binder delegate is
used to apply contextual data to a visual element.  
---|---  
[cellCreator](Search.SearchColumn-cellCreator.html)| If defined, the cell
creator delegate is used to customize how the search column displays its
information.  
[comparer](Search.SearchColumn-comparer.html)| If defined, the comparer
delegate is used to sort search results based on the value displayed in that
column.  
[content](Search.SearchColumn-content.html)| The content is used to display
the search column label and image in its header.  
[drawer](Search.SearchColumn-drawer.html)| If defined, the drawer delegate is
used to customize how the search column displays its information.  
[getter](Search.SearchColumn-getter.html)| If defined, the getter delegate is
used to customize how the search field data is extracted and transformed for
display (see SearchColumn.drawer).  
[name](Search.SearchColumn-name.html)| Name of the search column.  
[options](Search.SearchColumn-options.html)| Various options used to define
how a search column is presented.  
[path](Search.SearchColumn-path.html)| The path can be used by the column
delegates to interpret how the data can be manipulated.  
[provider](Search.SearchColumn-provider.html)| The provider is used to
indicate which search column provider (see SearchColumn) is used to define the
search column format.  
[selector](Search.SearchColumn-selector.html)| The selector is used by the
column delegates to fetch the search field data.  
[setter](Search.SearchColumn-setter.html)| If defined, the setter delegate
writes back the value to the corresponding field of the search result.  
[width](Search.SearchColumn-width.html)| The column width is used to set the
Search Table view column width.  
  
### Constructors

[SearchColumn](Search.SearchColumn-ctor.html)| Creates a new search column.  
---|---  
  
### Public Methods

[InitFunctors](Search.SearchColumn.InitFunctors.html)| Initialize the column
provider functors.  
---|---  
  
### Static Methods

[Enumerate](Search.SearchColumn.Enumerate.html)| Enumerate a set of columns
for a variety of search items.  
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

