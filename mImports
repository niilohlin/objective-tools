
badImports=$(grep -rn --include \*.[mh] ".m\"" ./ | grep import | sed -E 's/(.*\:[0-9]*\:).*/\1 .m import/g')
if [ $(echo "$badImports" | sed -e '/^$/d' | wc -l) -gt 0 ]
then
echo "$badImports"
exit 1
fi
