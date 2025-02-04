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

#
[IPropertyDatabaseView](Search.IPropertyDatabaseView.html).IsPersistableType

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

public bool IsPersistableType(Type type);

### Parameters

type | A type.  
---|---  
  
### Returns

**bool** True if the type can be persisted in the file, false otherwise.

### Description

Returns a boolean indicating if a type can be persisted into the backing file.

Only certain types can be persisted in the backing file to survive a domain
reload and quitting Unity. However, any type can be stored without backing in
the [PropertyDatabase](Search.PropertyDatabase.html). You can always decompose
your custom objects into smaller properties that can be persisted if you
absolutely need persistence.

    
    
    // Any object can be stored in the property database, but only
    // some of them will be persisted in the database file. All others
    // will disappear after the current Unity session. If you absolutely need your
    // data to be persisted, you can decompose your it into smaller properties that can
    // be serialized.
    using (var view = propertyDatabase.GetView())
    {
        var customTypeValue = new MyCustomType(42, "myValue");
        if (view.IsPersistableType(typeof(MyCustomType)))
        {
            var stored = view.Store("path/to/my/asset", "m_customTypeValue", customTypeValue);
            if (!stored)
                [Debug.LogWarning](Debug.LogWarning.html)("Property m_customTypeValue did not store.");
        }
        else
        {
            var stored = view.Store("path/to/my/asset", "m_customTypeValue.value", customTypeValue.value);
            if (!stored)
                [Debug.LogWarning](Debug.LogWarning.html)("Property m_customTypeValue.value did not store.");
            stored = view.Store("path/to/my/asset", "m_customTypeValue.name", customTypeValue.name);
            if (!stored)
                [Debug.LogWarning](Debug.LogWarning.html)("Property m_customTypeValue.name did not store.");
        }
    }
    

Additional resources:
[PropertyDatabaseType](Search.PropertyDatabaseType.html).

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

