[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-manifestPkg.html)
  * [中文](/cn/current/Manual/upm-manifestPkg.html)
  * [日本語](/ja/current/Manual/upm-manifestPkg.html)
  * [한국어](/kr/current/Manual/upm-manifestPkg.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-manifestPkg.html)
  * [中文](/cn/current/Manual/upm-manifestPkg.html)
  * [日本語](/ja/current/Manual/upm-manifestPkg.html)
  * [한국어](/kr/current/Manual/upm-manifestPkg.html)

  * [Packages and feature sets](PackagesList.html)
  * [Creating custom packages](CustomPackages.html)
  * Package manifest

[](cus-samples.html)

Creating samples for packages

[](upm-semver.html)

Versioning

# Package manifest

Unity uses a **package manifest** file (`package.json`) to manage information
about a specific version of a specific package. The package manifest is always
at the root of the package and has crucial information about the package, such
as its registered name and version number.

The package manifest also defines useful information to communicate to the
user, such as:

  * A user-friendly name that appears in the UI.
  * A brief description of the package.
  * The earliest version of the Unity Editor the package is compatible with.

The package manifest uses JSON (JavaScript Object Notation) syntax to describe
what’s inside the package. The file’s format is similar to
[npm](https://www.npmjs.com/)’s `package.json` format, but uses different
semantics for some of its properties. Refer to the example for a sample
package manifest file.

The Package Manager reads this manifest to find out the package’s contents,
how to unpack its contents, and what information to display in the [Package
Manager window](upm-ui.html). The manifest stores this information in a series
of required, recommended, and optional properties.

## Required properties

If these properties aren’t present, either the registry refuses the package
when it’s published, or the Package Manager can’t fetch or load the package.

**Property** | **JSON Type** | **Description**  
---|---|---  
**name** | String | A unique identifier that conforms to the Unity Package Manager naming convention, which uses reverse domain name notation. For more information about the naming convention, refer to [Naming your package](cus-naming.html).  
  
**Note** : The `name` identifier is different than the user-friendly display
name that appears in the [list panel](upm-ui-list.html) in the **Package
Manager** window.  
**version** | String | The package version number, which uses the format `"major.minor.patch"`.   
  
For example, `"3.2.1"` indicates that this is the 3rd major release, the 2nd
minor release, and the 1st patch.  
  
This value must respect [Semantic Versioning](http://semver.org/). For more
information, refer to [Versioning](upm-semver.html).  
  
## Recommended properties

The Package Manager can install packages in a project even if the recommended
properties are missing or have invalid values.

However, the recommended best practice is to assign values for these
properties to make sure that your package is discoverable and to offer a
better experience for users.

**Property** | **JSON Type** | **Description**  
---|---|---  
**description** | String | A brief description of the package. This is the text that appears in the [details panel](upm-ui-details.html) of the **Package Manager** window. This field supports [UTF–8](https://en.wikipedia.org/wiki/UTF-8) character codes. This means that you can use special formatting character codes, such as line breaks (`\n`) and bullets (`\u25AA`).  
**displayName** | String | A user-friendly name that appears in the Unity Editor (for example, in the **Project** window, the **Package Manager** window, etc.).   
  
Examples of `displayName` values are **Unity Timeline** , **ProBuilder** , and
**In App Purchasing**.  
**unity** | String | Indicates the lowest Unity version the package is compatible with. If omitted, the Package Manager considers the package compatible with all Unity versions.   
  
The expected format is `"major.minor"` (for example, `"2018.3"`). Unity 6 and
later versions follow the same `"####.#"` format. For example, the technical
version number for Unity 6 is `"6000.0"`.  
  
To point to a specific patch, also include the `unityRelease` property,
described in Optional properties.  
  
**Note** : A package that isn’t compatible with Unity doesn’t appear in the
[Package Manager window](upm-ui.html).  
  
## Optional properties

These properties are optional, meaning that you can omit them. However, if
they’re present, they must have a valid value.

**Property** | **JSON Type** | **Description**  
---|---|---  
**author** | Object or string | The author of the package. This property supports only one author.   
  
This property has one required field, **name** , and two optional fields,
**email** and **url**.  
  
You can specify these fields as a JSON object, or collapse them into a single
string whose key is **author**.  
  
Object example:  
`{`  
`"name" : "John Doe",`  
`"email" : "john.doe@example.com",`  
`"url" : "http://john.doe.example.com/"`  
`}`  
  
String example:  
`"John Doe <john.doe@example.com> (http://john.doe.example.com/)"`  
**changelogUrl** | String | Custom location for this package’s changelog specified as a URL. For example:  
`"changelogUrl": "https://example.com/changelog.html"`  
  
**Note** : When the Package Manager can’t reach the URL location (for example,
if there is a network issue), it does the following:  
  
\- If the package is installed, the Package Manager opens a file browser
displaying the `CHANGELOG.md` file in the package cache.  
\- If the package isn’t installed, the Package Manager displays a warning that
an offline changelog isn’t available.  
**dependencies** | Object | A map of package dependencies. Keys are package names, and values are specific versions. They identify other packages that this package depends on.   
  
**Note** : The Package Manager doesn’t support range syntax, only **SemVer**
versions.  
**documentationUrl** | String | Custom location for this package’s documentation, specified as a URL. For example:  
`"documentationUrl": "https://example.com/"`  
  
**Note** : When the Package Manager can’t reach the URL location (for example,
if there is a network issue), it does the following:  
  
\- If the package is installed, the Package Manager opens a file browser
displaying the `Documentation~` folder in the package cache.  
\- If the package isn’t installed, the Package Manager displays a warning that
offline documentation isn’t available.  
**hideInEditor** | Boolean | By default, the **Project** window hides package’s assets and omits them from the results when you use the [Object Picker](EditingValueProperties.html#ref-assign-objectpicker) in the **Inspector** window. Set this property to `"false"` to make sure that this package’s assets are always visible.  
**keywords** | Array of Strings | An array of keywords used by the Package Manager search APIs. This helps users find relevant packages.  
**license** | String | Identifier for an OSS license using the [SPDX identifier format](https://spdx.org/licenses/), or a string such as “Refer to LICENSE.md file”.  
  
**Note** : If you omit this property in your package manifest, your package
must contain a `LICENSE.md` file.  
**licensesUrl** | String | Custom location for this package’s license information, specified as a URL. For example:  
`"licensesUrl": "https://example.com/licensing.html"`  
  
**Note** : If the Package Manager can’t reach the URL location (for example,
if there is a network issue), it does the following:  
  
\- If the package is installed, it opens a file browser displaying the
`LICENSE.md` file in the package cache.  
\- If the package isn’t installed, the Package Manager displays a warning that
offline license information isn’t available.  
**samples** | Array of Objects | List of samples included in the package. Each sample has a display name, a description, and the path to the sample folder starting at the `Samples~` folder:  
  
`{`  
`"displayName": "<name-to-appear-in-the-UI>",`  
`"description": "<brief-description>",`  
`"path": "Samples~/<sample-subfolder>"`  
`}`  
  
For more information, refer to [Creating samples for packages](cus-
samples.html).  
**type** | String | **Reserved for internal use.**  
**unityRelease** | String | Part of a Unity version indicating the specific release of Unity that the package is compatible with. You can use this property when an updated package requires changes made during the Unity alpha/beta development cycle. This might be the case if the package needs newly introduced APIs, or uses existing APIs that have changed in a non-backward-compatible way without [API Updater](APIUpdater.html) rules.   
  
The expected format is `"<update><release>` (for example, `"0b4"`).  
  
**Note** : If you omit the recommended unity property, this property has no
effect.  
  
A package that isn’t compatible with Unity doesn’t appear in the [Package
Manager window](upm-ui.html).  
  
## Package manifest example

    
    
    {
      "name": "com.[company-name].[package-name]",
      "version": "1.2.3",
      "displayName": "Package Example",
      "description": "This is an example package",
      "unity": "2019.1",
      "unityRelease": "0b5",
      "documentationUrl": "https://example.com/",
      "changelogUrl": "https://example.com/changelog.html",
      "licensesUrl": "https://example.com/licensing.html",
      "dependencies": {
        "com.[company-name].some-package": "1.0.0",
        "com.[company-name].other-package": "2.0.0"
     },
     "keywords": [
        "keyword1",
        "keyword2",
        "keyword3"
      ],
      "author": {
        "name": "Unity",
        "email": "unity@example.com",
        "url": "https://www.unity3d.com"
      }
    }
    
    

## Additional resources

  * [Important Classes - Object](class-Object.html)

[](cus-samples.html)

Creating samples for packages

[](upm-semver.html)

Versioning

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

