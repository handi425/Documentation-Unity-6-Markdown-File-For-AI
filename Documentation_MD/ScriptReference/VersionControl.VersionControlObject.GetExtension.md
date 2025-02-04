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
[VersionControlObject](VersionControl.VersionControlObject.html).GetExtension

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

public T GetExtension();

### Returns

**T** Extension object if it's supported by
[VersionControlObject](VersionControl.VersionControlObject.html). **null**
otherwise.

### Description

Gets optional extension object.

You can implement optional extensions in your
[VersionControlObject](VersionControl.VersionControlObject.html) to improve
user experience. For example, the
[IIconOverlayExtension](VersionControl.IIconOverlayExtension.html) enables you
to draw VCS status overlays over asset icons. See the documentation for the
full list of extensions. Future versions of Unity might add new extensions or
stop calling existing ones.  
  
The default GetExtension implementation attempts to cast
[VersionControlObject](VersionControl.VersionControlObject.html) to extension
type. This allows you to implement extensions directly in your
[VersionControlObject](VersionControl.VersionControlObject.html) derived
class.

    
    
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    [VersionControl("Custom")]
    public class CustomVersionControlObject : [VersionControlObject](VersionControl.VersionControlObject.html), [IIconOverlayExtension](VersionControl.IIconOverlayExtension.html)
    {
        static [Texture2D](Texture2D.html) s_Icon;  
      
        static [Texture2D](Texture2D.html) GetIcon()
        {
            if (s_Icon == null)
            {
                s_Icon = new [Texture2D](Texture2D.html)(8, 8);
                for (var y = 0; y < s_Icon.height; ++y)
                {
                    for (var x = 0; x < s_Icon.width; ++x)
                    {
                        var border = y == 0 || y == s_Icon.height - 1 || x == 0 || x == s_Icon.width - 1;
                        var color = border ? [Color.white](Color-white.html) : [Color.red](Color-red.html);
                        s_Icon.SetPixel(x, y, color);
                    }
                }
                s_Icon.Apply();
            }
            return s_Icon;
        }  
      
        public void DrawOverlay(string assetPath, [IconOverlayType](VersionControl.IconOverlayType.html) type, [Rect](Rect.html) rect)
        {
            var topLeft = new [Rect](Rect.html)(rect.x, rect.y, 8, 8);
            var icon = GetIcon();
            [GUI.DrawTexture](GUI.DrawTexture.html)(topLeft, icon);
        }
    }
    

To support extensions implemented in separate classes you must overwrite this
method and return an appropriate object.

    
    
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class CustomIconOverlayExtension : [IIconOverlayExtension](VersionControl.IIconOverlayExtension.html)
    {
        public void DrawOverlay(string assetPath, [IconOverlayType](VersionControl.IconOverlayType.html) type, [Rect](Rect.html) rect)
        {
            var topLeft = new [Rect](Rect.html)(rect.x, rect.y, 8, 8);
            [GUI.DrawTexture](GUI.DrawTexture.html)(topLeft, [Texture2D.whiteTexture](Texture2D-whiteTexture.html));
        }
    }  
      
    [VersionControl("Custom")]
    public class CustomVersionControlObject : [VersionControlObject](VersionControl.VersionControlObject.html)
    {
        readonly [IIconOverlayExtension](VersionControl.IIconOverlayExtension.html) m_IconOverlayExtension = new CustomIconOverlayExtension();  
      
        public override T GetExtension<T>()
        {
            return m_IconOverlayExtension as T;
        }
    }
    

Additional resources:
[VersionControlObject](VersionControl.VersionControlObject.html),
[IIconOverlayExtension](VersionControl.IIconOverlayExtension.html),
[IInspectorWindowExtension](VersionControl.IInspectorWindowExtension.html),
[IPopupMenuExtension](VersionControl.IPopupMenuExtension.html),
[ISettingsInspectorExtension](VersionControl.ISettingsInspectorExtension.html).

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

